import yaml
import argparse


def get_settings(env, role, profile, outfile):

    # validate args
    if (env is None or env == "" or
        role is None or role == "" or
        profile is None or profile == "" or
        outfile is None or outfile == ""):
        print("Missing one of inputs, env, role, config out file")
        return 1
 
    try:
        with open(profile, 'r') as file:
            cfg = yaml.safe_load(file)
    except OSError as e:
        print(f"Error in opening config file [{e}]")
        return 2
    try:
        with open(outfile, 'a') as file:
            file.write(f"aws_account={cfg['aws'][env]['account']}\n")
            file.write(f"aws_region={cfg['aws'][env]['region']}\n")
            file.write(f"aws_audience={cfg['aws'][env]['audience']}\n")
            file.write(f"aws_role={cfg['role'][role]['name']}\n")
            file.write(f"aws_role_duration={cfg['role'][role]['duration']}\n")
            file.write(f"app_name={cfg['application']['name']}\n")
            file.write(f"app_registry={cfg['application']['package']['registry']}\n")
            file.write(f"pp_repository={cfg['application']['package']['repository']}\n")
            file.write(f"app_runtime={cfg['application']['runtime']['name']}\n")
            file.write(f"app_runtime_version={cfg['application']['runtime']['version']}\n")

    except KeyError as e:
        print(f"Incorrect key value [{e}]")
        return 3

    return 0


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', help='IS environment')
    parser.add_argument('--role', help='aws role')
    parser.add_argument('--profile', help='cicd configuration')
    parser.add_argument('--outfile', help='output file')

    args = vars(parser.parse_args())

    get_settings(args['env'], args['role'], args['profile'], args['outfile'])


if __name__ == "__main__":
    cli()
