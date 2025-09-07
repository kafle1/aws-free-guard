"""CLI commands for AWS Free Guard."""

import json
import time
from typing import List, Optional
import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Confirm

from src.models.aws_account import AWSAccount
from src.models.operation_result import OperationResult
from src.lib.aws_free import AWSFreeEnforcer
from src.lib.aws_clean import AWSCleaner

console = Console()

@click.group()
@click.option('--profile', default=None, help='AWS profile to use')
@click.option('--region', default='us-east-1', help='AWS region to use')
@click.pass_context
def cli(ctx, profile, region):
    """AWS Free Guard - Keep your AWS account safe within free tier limits."""
    ctx.ensure_object(dict)
    ctx.obj['profile'] = profile
    ctx.obj['region'] = region

@cli.command()
@click.pass_context
@click.option('--services', multiple=True, help='Specific services to analyze (default: all)')
@click.option('--all-regions', is_flag=True, help='Analyze all regions (default: current region only)')
@click.option('--output', type=click.Choice(['table', 'json', 'summary']), default='table', help='Output format')
@click.option('--detailed', is_flag=True, help='Show detailed analysis')
@click.option('--dry-run', is_flag=True, help='Preview changes without applying them')
def free(ctx, services, all_regions, output, detailed, dry_run):
    """Analyze AWS account and enforce free tier limits."""
    try:
        with console.status("[bold green]Initializing AWS Free Guard...", spinner="dots"):
            account = AWSAccount(profile_name=ctx.obj['profile'], region=ctx.obj['region'])
            enforcer = AWSFreeEnforcer(account)

        console.print("[bold blue]🔍 Starting comprehensive AWS analysis...[/bold blue]")

        # Perform comprehensive analysis
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Analyzing AWS resources...", total=None)

            if services:
                services_list = list(services)
            else:
                services_list = None

            analysis_results = enforcer.comprehensive_analysis(
                services=services_list,
                include_all_regions=all_regions,
                dry_run=dry_run
            )

            progress.update(task, completed=True)

        # Display results based on output format
        if output == 'json':
            console.print_json(json.dumps(analysis_results, indent=2, default=str))
        elif output == 'summary':
            _display_summary(analysis_results)
        else:
            _display_detailed_table(analysis_results, detailed)

        # Show recommendations
        if analysis_results.get('recommendations'):
            console.print("\n[bold yellow]💡 Recommendations:[/bold yellow]")
            for rec in analysis_results['recommendations']:
                console.print(f"  • {rec}")

        # Risk assessment
        risk = analysis_results.get('risk_assessment', {})
        if risk.get('overall_risk') == 'HIGH':
            console.print(f"\n[bold red]⚠️  HIGH RISK: {', '.join(risk.get('risk_factors', []))}[/bold red]")
        elif risk.get('overall_risk') == 'MEDIUM':
            console.print(f"\n[bold yellow]⚠️  MEDIUM RISK: {', '.join(risk.get('risk_factors', []))}[/bold yellow]")
        else:
            console.print(f"\n[bold green]✅ LOW RISK - Account appears safe[/bold green]")

        # Cost analysis
        cost_analysis = analysis_results.get('cost_analysis', {})
        if cost_analysis.get('total_monthly_cost', 0) > 0:
            console.print(f"\n[bold cyan]💰 Current Monthly Cost: ${cost_analysis['total_monthly_cost']:.2f}[/bold cyan]")

        # Predictions
        predictions = analysis_results.get('predictions', {})
        if predictions.get('next_month_prediction', 0) > 0:
            console.print(f"\n[bold magenta]🔮 Predicted Next Month: ${predictions['next_month_prediction']:.2f}[/bold magenta]")

    except Exception as e:
        console.print(f"[bold red]❌ Error: {str(e)}[/bold red]")
        raise click.Abort()

@cli.command()
@click.pass_context
@click.option('--services', multiple=True, help='Specific services to clean (default: all)')
@click.option('--all-regions', is_flag=True, help='Clean all regions (default: current region only)')
@click.option('--dry-run', is_flag=True, help='Show what would be cleaned without actually doing it')
@click.option('--force', is_flag=True, help='Skip confirmation prompts')
@click.option('--confirm', is_flag=True, help='Automatically confirm the operation')
def clean(ctx, services, all_regions, dry_run, force, confirm):
    """Clean AWS account by removing unused resources."""
    try:
        with console.status("[bold green]Initializing AWS Cleaner...", spinner="dots"):
            account = AWSAccount(profile_name=ctx.obj['profile'], region=ctx.obj['region'])
            cleaner = AWSCleaner(account)

        if not force and not dry_run and not confirm:
            if not Confirm.ask("⚠️  This will delete resources from your AWS account. Continue?"):
                console.print("[yellow]Operation cancelled.[/yellow]")
                return

        console.print("[bold red]🧹 Starting AWS account cleanup...[/bold red]")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Cleaning AWS resources...", total=None)

            if services:
                services_list = list(services)
            else:
                services_list = None

            clean_results = cleaner.comprehensive_clean(
                services=services_list,
                include_all_regions=all_regions,
                dry_run=dry_run
            )

            progress.update(task, completed=True)

        # Display clean results
        _display_clean_results(clean_results, dry_run)

    except Exception as e:
        console.print(f"[bold red]❌ Error: {str(e)}[/bold red]")
        raise click.Abort()

@cli.command()
@click.pass_context
@click.option('--days', default=30, help='Number of days to analyze')
@click.option('--output', type=click.Choice(['table', 'json']), default='table', help='Output format')
def cost(ctx, days, output):
    """Analyze AWS costs and usage patterns."""
    try:
        with console.status("[bold green]Initializing cost analyzer...", spinner="dots"):
            account = AWSAccount(profile_name=ctx.obj['profile'], region=ctx.obj['region'])
            enforcer = AWSFreeEnforcer(account)

        console.print(f"[bold cyan]💰 Analyzing costs for the last {days} days...[/bold cyan]")

        cost_analysis = enforcer.cost_analyzer.analyze_costs()

        if output == 'json':
            console.print_json(json.dumps(cost_analysis, indent=2, default=str))
        else:
            _display_cost_analysis(cost_analysis)

    except Exception as e:
        console.print(f"[bold red]❌ Error: {str(e)}[/bold red]")
        raise click.Abort()

@cli.command()
@click.pass_context
def status(ctx):
    """Show current AWS account status and health."""
    try:
        with console.status("[bold green]Checking AWS account status...", spinner="dots"):
            account = AWSAccount(profile_name=ctx.obj['profile'], region=ctx.obj['region'])
            account_id = account.get_account_id()

        console.print(f"[bold green]✅ AWS Account: {account_id}[/bold green]")
        console.print(f"[bold blue]📍 Region: {account.region}[/bold blue]")
        console.print(f"[bold cyan]🔧 Profile: {ctx.obj['profile'] or 'default'}[/bold cyan]")

        # Quick resource count
        enforcer = AWSFreeEnforcer(account)
        analysis = enforcer.comprehensive_analysis(include_all_regions=False)

        total_resources = analysis.get('total_resources_found', 0)
        risk_level = analysis.get('risk_assessment', {}).get('overall_risk', 'UNKNOWN')

        console.print(f"[bold magenta]📊 Total Resources: {total_resources}[/bold magenta]")
        console.print(f"[bold yellow]⚠️  Risk Level: {risk_level}[/bold yellow]")

    except Exception as e:
        console.print(f"[bold red]❌ Error: {str(e)}[/bold red]")
        raise click.Abort()

@cli.command()
@click.pass_context
@click.option('--backup-dir', default='./aws-backup', help='Directory to store backup')
@click.option('--services', multiple=True, help='Specific services to backup (default: all)')
def backup(ctx, backup_dir, services):
    """Create backup of AWS resources configuration."""
    try:
        with console.status("[bold green]Initializing backup...", spinner="dots"):
            account = AWSAccount(profile_name=ctx.obj['profile'], region=ctx.obj['region'])
            enforcer = AWSFreeEnforcer(account)

        console.print(f"[bold blue]💾 Creating backup in {backup_dir}...[/bold blue]")

        # This would implement actual backup functionality
        console.print("[green]✅ Backup completed (placeholder)[/green]")

    except Exception as e:
        console.print(f"[bold red]❌ Error: {str(e)}[/bold red]")
        raise click.Abort()

def _display_summary(analysis_results: dict):
    """Display summary of analysis results."""
    total_resources = analysis_results.get('total_resources_found', 0)
    regions = len(analysis_results.get('regions_analyzed', []))
    cost = analysis_results.get('cost_analysis', {}).get('total_monthly_cost', 0)
    risk = analysis_results.get('risk_assessment', {}).get('overall_risk', 'UNKNOWN')

    summary_table = Table(title="AWS Account Summary")
    summary_table.add_column("Metric", style="cyan")
    summary_table.add_column("Value", style="magenta")

    summary_table.add_row("Total Resources", str(total_resources))
    summary_table.add_row("Regions Analyzed", str(regions))
    summary_table.add_row("Monthly Cost", f"${cost:.2f}")
    summary_table.add_row("Risk Level", risk)

    console.print(summary_table)

def _display_detailed_table(analysis_results: dict, detailed: bool = False):
    """Display detailed analysis results in table format."""
    regions = analysis_results.get('regions_analyzed', [])

    for region_data in regions:
        region_name = region_data.get('region', 'unknown')
        services = region_data.get('services', {})

        region_table = Table(title=f"AWS Resources in {region_name}")
        region_table.add_column("Service", style="cyan")
        region_table.add_column("Resources", style="magenta", justify="right")
        region_table.add_column("Status", style="green")

        for service_name, service_data in services.items():
            resource_count = service_data.get('resource_count', 0)
            
            # Count charged resources
            charged_count = 0
            resources = service_data.get('resources', [])
            if resources:
                for resource in resources:
                    if isinstance(resource, dict):
                        status = resource.get('status', 'unknown')
                    else:
                        status = getattr(resource, 'status', 'unknown')
                    if status == 'ResourceStatus.CHARGED' or (hasattr(status, 'value') and status.value == 'charged'):
                        charged_count += 1
            
            status = "✅ OK" if charged_count == 0 else "⚠️  Check"

            region_table.add_row(service_name.upper(), str(charged_count), status)

        console.print(region_table)

        if detailed:
            # Show detailed resources per service
            for service_name, service_data in services.items():
                if service_data.get('resource_count', 0) > 0:
                    console.print(f"\n[yellow]Resources in {service_name.upper()} for {region_name}:[/yellow]")
                    resources = service_data.get('resources', [])
                    if resources:
                        for resource in resources:
                            if isinstance(resource, dict):
                                resource_id = resource.get('resource_id', 'unknown')
                                resource_type = resource.get('resource_type', 'unknown')
                                status = resource.get('status', 'unknown')
                            else:
                                resource_id = getattr(resource, 'resource_id', 'unknown')
                                resource_type = getattr(resource, 'resource_type', 'unknown')
                                status = getattr(resource, 'status', 'unknown')
                            console.print(f"  • {resource_type}: {resource_id} ({status})")

            # Show recommendations per region
            recommendations = region_data.get('recommendations', [])
            if recommendations:
                console.print(f"\n[yellow]Recommendations for {region_name}:[/yellow]")
                for rec in recommendations:
                    console.print(f"  • {rec}")

def _display_clean_results(clean_results: dict, dry_run: bool):
    """Display cleanup results."""
    if dry_run:
        console.print("[bold yellow]🔍 DRY RUN - No resources were actually deleted[/bold yellow]")
    else:
        console.print("[bold red]🗑️  Resources cleaned from AWS account[/bold red]")

    # Display what was cleaned
    cleaned_resources = clean_results.get('cleaned_resources', [])
    if cleaned_resources:
        clean_table = Table(title="Cleaned Resources")
        clean_table.add_column("Resource ID", style="cyan")
        clean_table.add_column("Service", style="magenta")
        clean_table.add_column("Type", style="yellow")

        for resource in cleaned_resources:
            clean_table.add_row(
                resource.get('resource_id', 'unknown'),
                resource.get('service', 'unknown'),
                resource.get('resource_type', 'unknown')
            )

        console.print(clean_table)
    else:
        console.print("[green]✨ No resources needed cleaning[/green]")

def _display_cost_analysis(cost_analysis: dict):
    """Display cost analysis results."""
    total_cost = cost_analysis.get('total_monthly_cost', 0)
    service_breakdown = cost_analysis.get('service_breakdown', {})

    console.print(f"[bold cyan]💰 Total Monthly Cost: ${total_cost:.2f}[/bold cyan]")

    if service_breakdown:
        cost_table = Table(title="Cost Breakdown by Service")
        cost_table.add_column("Service", style="cyan")
        cost_table.add_column("Cost", style="magenta", justify="right")

        for service, cost in service_breakdown.items():
            cost_table.add_row(service, f"${cost:.2f}")

        console.print(cost_table)

if __name__ == '__main__':
    cli()
