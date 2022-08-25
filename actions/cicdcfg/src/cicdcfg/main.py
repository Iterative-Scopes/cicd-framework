import yaml
import argparse


def get_settings(env, role, profile):

    # validate args
    if (env is None or env == "" or
        role is None or role == "" or
        profile is None or profile == ""):
        print("Missing one of inputs, env, role or config file")
        return 1
 
    try:
        with open(profile, 'r') as file:
            cfg = yaml.safe_load(file)
    except OSError as e:
        print(f"Error in opening config file [{e}]")
        return 2
    try:
        print(f"::set-output name=aws_account::{cfg['aws'][env]['account']}")
        print(f"::set-output name=aws_region::{cfg['aws'][env]['region']}")
        print(f"::set-output name=aws_audience::{cfg['aws'][env]['audience']}")
        print(f"::set-output name=aws_role::{cfg['role'][role]['name']}")
        print(f"::set-output name=aws_role_duration::{cfg['role'][role]['duration']}")
        print(f"::set-output name=app_name::{cfg['application']['name']}")
        print(f"::set-output name=app_registry::{cfg['application']['package']['registry']}")
        print(f"::set-output name=app_repository::{cfg['application']['package']['repository']}")
        print(f"::set-output name=app_name::{cfg['application']['runtime']['name']}")
        print(f"::set-output name=app_version::{cfg['application']['runtime']['version']}")

    except KeyError as e:
        print(f"Incorrect key value [{e}]")
        return 3

    return 0


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', help='IS environment')
    parser.add_argument('--role', help='aws role')
    parser.add_argument('--profile', help='cicd configuration')

    args = vars(parser.parse_args())

    get_settings(args['env'], args['role'], args['profile'])


if __name__ == "__main__":
    cli()
