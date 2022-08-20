import os


def main():
    is_env = os.environ["IS_ENV"]
    mode = os.environ["IS_MODE"]

    my_output = f"[{is_env}]-[{mode}]"

    print(f"::set-output name=aws_account::{my_output}")
    print(f"::set-output name=aws_role::{my_output}")
    os.environ["IS_AWS_ACCOUNT"] = my_output

if __name__ == "__main__":
    main()
