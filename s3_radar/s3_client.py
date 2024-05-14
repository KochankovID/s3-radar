import time
from pathlib import Path

import boto3
from tqdm import tqdm

from s3_radar.constants import BYTES_IN_MEGABYTE


def upload_file(
    generated_file: Path,
    file_size: int,
    target_file_path: str,
    bucket: str,
    ak: str,
    sak: str,
    endpoint: str = "https://obs.ru-moscow-1.hc.sbercloud.ru",
) -> None:
    session = boto3.Session(
        aws_access_key_id=ak,
        aws_secret_access_key=sak,
    )

    client = session.client(
        "s3",
        endpoint_url=endpoint,
    )

    start_time = time.time()
    with tqdm(
        total=file_size,
        desc=f"s3://{target_file_path}",
        bar_format="Upload: {percentage:.1f}%|{bar:25} | {rate_fmt} | {desc}",
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as pbar:
        client.upload_file(
            generated_file,
            bucket,
            target_file_path,
            Callback=pbar.update,
        )
    end_time = time.time()
    upload_time_seconds = end_time - start_time

    print(f"Upload {file_size / BYTES_IN_MEGABYTE} mb for {upload_time_seconds:.2f} seconds")
    print(f"Speed: {file_size / BYTES_IN_MEGABYTE / upload_time_seconds:.2f} mb/s")


def download_file(
    s3_file_path: str,
    local_file_path: Path,
    file_size: int,
    bucket: str,
    ak: str,
    sak: str,
    endpoint: str = "https://obs.ru-moscow-1.hc.sbercloud.ru",
) -> None:
    session = boto3.Session(
        aws_access_key_id=ak,
        aws_secret_access_key=sak,
    )

    client = session.client(
        "s3",
        endpoint_url=endpoint,
    )

    start_time = time.time()
    with tqdm(
        total=file_size,
        desc=f"s3://{s3_file_path}",
        bar_format="Download: {percentage:.1f}%|{bar:25} | {rate_fmt} | {desc}",
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as pbar:
        client.download_file(
            bucket,
            s3_file_path,
            local_file_path,
            Callback=pbar.update,
        )
    end_time = time.time()
    download_time_seconds = end_time - start_time

    print(f"Download {file_size / BYTES_IN_MEGABYTE} mb for {download_time_seconds:.2f} seconds")
    print(f"Speed: {file_size / BYTES_IN_MEGABYTE / download_time_seconds:.2f} mb/s")
