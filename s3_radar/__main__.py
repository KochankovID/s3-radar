from typing import Annotated

import typer

from s3_radar.constants import BYTES_IN_MEGABYTE
from s3_radar.data_generator import build_target_file_path, generate_file
from s3_radar.s3_client import download_file, upload_file

app = typer.Typer()


@app.command(name="up")
def upload_speed(
    bucket: str,
    ak: str,
    sak: str,
    endpoint: str = "https://obs.ru-moscow-1.hc.sbercloud.ru",
    megabyte_size: Annotated[int, typer.Option("-s")] = 1024,
) -> None:
    """
    Test S3 upload speed.
    """

    file_size = megabyte_size * BYTES_IN_MEGABYTE
    generated_file = generate_file(megabyte_size * BYTES_IN_MEGABYTE)
    target_file_path = build_target_file_path(generated_file)
    upload_file(
        generated_file=generated_file,
        file_size=file_size,
        target_file_path=target_file_path,
        bucket=bucket,
        ak=ak,
        sak=sak,
        endpoint=endpoint,
    )
    generated_file.unlink()


@app.command(name="down")
def download_speed(
    bucket: str,
    ak: str,
    sak: str,
    endpoint: str = "https://obs.ru-moscow-1.hc.sbercloud.ru",
    megabyte_size: Annotated[int, typer.Option("-s")] = 1024,
) -> None:
    """
    Test S3 upload and download speed.
    """
    file_size = megabyte_size * BYTES_IN_MEGABYTE
    generated_file = generate_file(megabyte_size * BYTES_IN_MEGABYTE)
    target_file_path = build_target_file_path(generated_file)
    upload_file(
        generated_file=generated_file,
        file_size=file_size,
        target_file_path=target_file_path,
        bucket=bucket,
        ak=ak,
        sak=sak,
        endpoint=endpoint,
    )
    download_file(
        s3_file_path=target_file_path,
        local_file_path=generated_file,
        file_size=file_size,
        bucket=bucket,
        ak=ak,
        sak=sak,
        endpoint=endpoint,
    )
    generated_file.unlink()


if __name__ == "__main__":
    app()
