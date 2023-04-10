import sys
import anyio
import dagger

async def markdown_lint():

    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        src = client.host().directory("./packages")
        ci = client.host().directory("./.ci/scripts")

        lint = (
            client.container().from_("debian:bullseye")
            .with_exec("apt update".split(" "))
            .with_exec("apt install tree".split(" "))
            .with_mounted_directory("/data", src)
            .with_mounted_directory("/scripts", ci)
            .with_workdir("/data")
            .with_exec("tree".split(" "))
            .with_exec("/scripts/compile-deb.sh".split(" "))
        )

        await lint.stdout()
    print(f"Packaging is FINISHED!")

if __name__ == "__main__":
    try:
        anyio.run(markdown_lint)
    except:
        print("Error")
