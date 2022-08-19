import os


def main():
    is_env = os.environ["INPUT_IS_ENV"]
    mode = os.environ["INPUT_MODE"]

    my_output = f"[{is_env}]-[{mode}]"

    print(f"::set-output name=aws_account::{my_output}")
    print(f"::set-output name=aws_role::{my_output}")


if __name__ == "__main__":
    main()
