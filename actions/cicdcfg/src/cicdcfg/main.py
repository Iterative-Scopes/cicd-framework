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
        print(f"::set-output name=aws_role::{cfg['role'][role]['name']}")
        print(f"::set-output name=aws_role_duration::{cfg['role'][role]['duration']}")
        print(f"::set-output name=app_name::{cfg['application']['name']}")
        print(f"::set-output name=app_runtime::{cfg['application']['runtime']['name']}")
        print(f"::set-output name=app_runtime_version::{cfg['application']['runtime']['version']}")
        
        for key in cfg['application']['package']:
            print(f"name=app_{key}::{cfg['application']['package'][key]}")
            print(f"::set-output name=app_{key}::{cfg['application']['package'][key]}")
        for key in cfg['aws'][env]:
            print(f"name=aws_{key}::{cfg['aws'][env][key]}")
            print(f"::set-output name=aws_{key}::{cfg['aws'][env][key]}")

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
