"""Bounded OCP 7.9.3.1.1 call-shape inventory controller.

This file has three disjoint modes.  Controller and validator modes never import
OCP.  Inventory mode is the only native-importing path and performs exactly one
preselected zero-argument version call after its installed stub proves that call
shape.  The file is content-frozen and externally hashed before controller mode
is ever invoked.
"""

from __future__ import annotations

import argparse
import ast
import base64
import csv
import ctypes
from ctypes import wintypes
import datetime as dt
import email.parser
import hashlib
import importlib
import importlib.metadata
import importlib.util
import inspect
import io
import json
import os
from pathlib import Path, PurePosixPath
import platform
import re
import shutil
import stat
import struct
import subprocess
import sys
import threading
import time
import traceback
import zipfile
import math


PLAN_SHA256 = "dfa54caed0897847f6e11709d5b5149f292186779add1f21144e3a5f1ea6f689"
V2_PLAN_SHA256 = "89ea6939c477a22e18a84ecd4805b298ddd601adce24661a47f2e9c31bc2ce07"
RETIRED_PLAN_SHA256 = "ca9543a84316051156471c41a71656303ebcf25426199c8d3f3744c1c203df84"
FOUNDATION_COMMIT = "23b441c3fcabb5bf4cf077daca882b984f978b42"
FOUNDATION_TREE = "a996a21a31c775660eb9dac3d491160231ba8cc1"
HOST_PYTHON = Path(r"C:\Python\Python313\python.exe")
TASK_ROOT = Path(
    r"C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-ocp-79311-inventory-v3"
)
FINAL_ROOT = Path(
    r"C:\Github\ANYopenSoft\governance\evidence\ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V3"
)
PENDING_ROOT = Path(
    r"C:\Github\ANYopenSoft\governance\evidence\.ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V3.pending"
)
SENTRY_TEMP = Path(
    r"C:\Github\ANYopenSoft\governance\evidence\.ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V3.staging-sentry.tmp"
)
SENTRY = Path(
    r"C:\Github\ANYopenSoft\governance\evidence\.ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V3.staging-sentry"
)
SENTRY_PAYLOAD = b"ANYfileio-occt OCP inventory v3 staging sentry\n"
V2_TASK_ROOT = Path(
    r"C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-ocp-79311-inventory-v2"
)
V2_WHEELHOUSE = V2_TASK_ROOT / "wheelhouse"
V2_FINAL_ROOT = Path(
    r"C:\Github\ANYopenSoft\governance\evidence\ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY_V2"
)
V2_PENDING_ROOT = V2_FINAL_ROOT.with_name("." + V2_FINAL_ROOT.name + ".pending")
V2_SENTRY_TEMP = V2_FINAL_ROOT.with_name("." + V2_FINAL_ROOT.name + ".staging-sentry.tmp")
V2_SENTRY = V2_FINAL_ROOT.with_name("." + V2_FINAL_ROOT.name + ".staging-sentry")
V2_PROBE_SHA256 = "3a86fb437e804a0cb0ed205c1a41ff536b61300f38ae4f08945bfef7b0c3eed6"
V2_OUTCOME_SHA256 = "a65e85d0a4f0ca01020e0c9eaa76b6683bf29afe7289b4f55b1cded839821042"
V2_SUMS_SHA256 = "f4cad6876d537dd905a7aaecb4fe896a87d225b5ed06d2e54c97cb5155a3a993"
V2_FINAL_BYTES = 145235
RETIRED_RECEIPT = Path(
    r"C:\Github\ANYopenSoft\governance\evidence\.ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY.pending"
)
RETIRED_FINAL_ROOT = Path(
    r"C:\Github\ANYopenSoft\governance\evidence\ANYFILEIO_OCCT_OCP_7_9_3_1_1_CP313_WIN_AMD64_INVENTORY"
)
RETIRED_RECEIPT_SUMS_SHA256 = (
    "5ab56f7750daa11650fecf698f108435a08b0083e0525a43106bfb3414e5a7f5"
)
RETIRED_RECEIPT_OUTCOME_SHA256 = (
    "d996aeaf89b7a6248601b7b00e8393664a874883af753e9eef0eeb3608efbab7"
)
RETIRED_RECEIPT_BYTES = 134002
FOUNDATION_ROOT = Path(
    r"C:\Users\AudunArnesenNyhus\AppData\Local\Temp\codex-anyfileio-occt-native-foundation"
)
EVIDENCE_NAMES = (
    "PROBE.py",
    "WHEELS.json",
    "API_INVENTORY.json",
    "OUTCOME.json",
    "STDOUT.txt",
    "STDERR.txt",
    "SHA256SUMS.txt",
)
HASHED_EVIDENCE_NAMES = tuple(sorted(EVIDENCE_NAMES[:-1]))
ATTEMPT_ONE = {
    "attempt": 1,
    "status": "BLOCKED",
    "plan_sha256": RETIRED_PLAN_SHA256,
    "probe_sha256": "90856d3347dc4728da9bd4c715f3ed515784c29115554027a3f15c8f2bea7677",
    "exit_code": 1,
    "wall_seconds": 0.6,
    "failure": {
        "type": "builtins.FileNotFoundError",
        "stage": "evidence-staging",
        "winerror": 3,
        "message": (
            "The registered evidence parent was absent while creating the pending "
            "seven-file bundle"
        ),
    },
    "observed_after_exit": {
        "https_gets_started": 0,
        "wheel_files": 0,
        "venv_created": False,
        "install_started": False,
        "ocp_imported": False,
        "pending_created": False,
        "final_created": False,
        "residual_task_processes": 0,
    },
}
ATTEMPT_TWO = {
    "attempt": 2,
    "status": "BLOCKED",
    "plan_sha256": RETIRED_PLAN_SHA256,
    "probe_sha256": "ae22c292cc9e9fe03bfb57e46653e6d34314876009f7c98994d421db5c5aa44f",
    "exit_code": 2,
    "wall_seconds": 0.111471,
    "failure": {
        "type": "BLOCKED",
        "stage": "resource",
        "message": "foundation-identity left an unexpected descendant",
    },
    "observed_after_exit": {
        "https_gets_started": 0,
        "wheel_files": 0,
        "venv_created": False,
        "install_started": False,
        "ocp_imported": False,
        "pending_created": False,
        "final_created": False,
        "residual_task_processes": 0,
        "wheel_status": "NOT_RUN",
        "api_status": "NOT_RUN",
        "stdout_bytes": 0,
        "stderr_bytes": 0,
    },
}
ATTEMPT_THREE = {
    "attempt": 3,
    "status": "BLOCKED",
    "plan_sha256": V2_PLAN_SHA256,
    "probe_sha256": V2_PROBE_SHA256,
    "exit_code": 2,
    "wall_seconds": 6.254012,
    "failure": {
        "type": "BLOCKED",
        "stage": "wheel",
        "message": "directory member not represented in RECORD: cadquery_ocp_novtk.libs/",
    },
    "observed_after_exit": {
        "https_gets_started": 3,
        "https_gets_completed_200": 3,
        "wheel_files": 3,
        "venv_created": False,
        "install_started": False,
        "ocp_imported": False,
        "inventory_status": "NOT_RUN",
        "secondary_failures": 0,
        "final_created": True,
    },
}
ATTEMPT_HISTORY = (ATTEMPT_ONE, ATTEMPT_TWO, ATTEMPT_THREE)
PREDECESSOR_RECEIPT = {
    "path": str(V2_FINAL_ROOT),
    "file_count": 7,
    "bytes": V2_FINAL_BYTES,
    "sha256sums_sha256": V2_SUMS_SHA256,
    "outcome_sha256": V2_OUTCOME_SHA256,
}

MIB = 1024 * 1024
HASH_CHUNK = MIB
MAX_WHEEL_MEMBERS = 4096
MAX_INSTALLED_FILES = 4096
MAX_PYI_FILES = 128
MAX_PYI_BYTES = 16 * MIB
MAX_PYI_TOTAL = 128 * MIB
MAX_DECLARATIONS = 256
MAX_DOC_BYTES = 16384
MAX_DOC_TOTAL = 2 * MIB
MAX_JSON_BYTES = 8 * MIB
MAX_JSON_DEPTH = 32
MAX_STREAM_BYTES = 8 * MIB
MAX_EVIDENCE_BYTES = 32 * MIB
MAX_TASK_BYTES = 1024 * MIB
TOTAL_SECONDS = 600.0
REUSE_SECONDS = 120.0
VENV_SECONDS = 180.0
INSTALL_SECONDS = 180.0
INVENTORY_SECONDS = 120.0
VALIDATE_SECONDS = 30.0
PUBLICATION_RESERVE_SECONDS = 30.0
ACTIVE_PROCESS_ZERO_GRACE_SECONDS = 10.0
JOB_POLL_SECONDS = 0.1
WORKER_ACTIVE_PROCESS_LIMIT = 3
WORKER_PROCESS_MEMORY_BYTES = 512 * MIB
WORKER_JOB_MEMORY_BYTES = 768 * MIB

WHEELS = (
    {
        "key": "novtk",
        "filename": "cadquery_ocp_novtk-7.9.3.1.1-cp313-cp313-win_amd64.whl",
        "url": "https://files.pythonhosted.org/packages/57/48/4595c22b0ae1b4759f209a13d21dadd229db6c374d9b0a95afa7ed0c4714/cadquery_ocp_novtk-7.9.3.1.1-cp313-cp313-win_amd64.whl",
        "bytes": 46364506,
        "sha256": "3390be6d8199a50b01ae0137a60f56d0cfecd8753dbee08532bbbeb8b7169682",
        "name": "cadquery-ocp-novtk",
        "version": "7.9.3.1.1",
        "requires_python": "<3.15,>=3.10",
        "requires_dist": ("cadquery-ocp-proxy",),
        "tag": "cp313-cp313-win_amd64",
        "member_count": 720,
        "file_member_count": 398,
        "directory_count": 322,
        "directory_attribute_counts": ((0, 0x41FF0010, 0, zipfile.ZIP_STORED, 322),),
        "file_attribute_counts": ((0, 0x81B60000, 0, zipfile.ZIP_DEFLATED, 398),),
    },
    {
        "key": "proxy",
        "filename": "cadquery_ocp_proxy-7.9.3.1.1-py3-none-any.whl",
        "url": "https://files.pythonhosted.org/packages/30/c0/04e9363a99fee892de2776820e3dcf04f8825b6edc9580efe3416c9465a7/cadquery_ocp_proxy-7.9.3.1.1-py3-none-any.whl",
        "bytes": 3322,
        "sha256": "ca4164ec4b54956d9fc3e68c67d555b5486cb963c2f71e18df005ba16b921c91",
        "name": "cadquery-ocp-proxy",
        "version": "7.9.3.1.1",
        "requires_python": ">=3.10",
        "requires_dist": (),
        "tag": "py3-none-any",
        "member_count": 7,
        "file_member_count": 5,
        "directory_count": 2,
        "directory_attribute_counts": ((3, 0x41ED0000, 0x800, zipfile.ZIP_STORED, 2),),
        "file_attribute_counts": ((3, 0x81A40000, 0x800, zipfile.ZIP_DEFLATED, 5),),
    },
    {
        "key": "stubs",
        "filename": "cadquery_ocp_stubs-7.9.3.1.1-py3-none-win_amd64.whl",
        "url": "https://files.pythonhosted.org/packages/6c/de/2a93a7cd47226bdd802674e8a040235ef1a1a4433bbf4d220e21253fe31e/cadquery_ocp_stubs-7.9.3.1.1-py3-none-win_amd64.whl",
        "bytes": 2899849,
        "sha256": "5ecba090df1ada12c558ff4a1b49c61d5155edc8cb3411067a785e3b43f4b359",
        "pep658_sha256": "514e4d3a8d0f6072ab94d766649a675a591bbcb55294faf28c01e546a8b8eec7",
        "name": "cadquery-ocp-stubs",
        "version": "7.9.3.1.1",
        "requires_python": "<3.15,>=3.10",
        "requires_dist": (),
        "tag": "py3-none-win_amd64",
        "member_count": 329,
        "file_member_count": 329,
        "directory_count": 0,
        "directory_attribute_counts": (),
        "file_attribute_counts": (
            (0, 0x81B60000, 0, zipfile.ZIP_DEFLATED, 328),
            (0, 0x81B40000, 0, zipfile.ZIP_DEFLATED, 1),
        ),
    },
)

TARGETS = (
    "OCP.Standard.Standard_Version_s",
    "OCP.Standard.Standard_Version",
    "OCP.Standard.Standard_Version_Complete_s",
    "OCP.Standard.Standard_Version_Complete",
    "OCP.Standard.Standard_Version_String_s",
    "OCP.Standard.Standard_Version_String",
    "OCP.XCAFApp.XCAFApp_Application.GetApplication_s",
    "OCP.XCAFApp.XCAFApp_Application.NewDocument",
    "OCP.XCAFApp.XCAFApp_Application.InitDocument",
    "OCP.XCAFApp.XCAFApp_Application.Close",
    "OCP.TDocStd.TDocStd_Document",
    "OCP.TDocStd.TDocStd_Document.Main",
    "OCP.TCollection.TCollection_ExtendedString",
    "OCP.XCAFDoc.XCAFDoc_DocumentTool.ShapeTool_s",
    "OCP.XCAFDoc.XCAFDoc_DocumentTool.ColorTool_s",
    "OCP.XCAFDoc.XCAFDoc_DocumentTool.LayerTool_s",
    "OCP.STEPCAFControl.STEPCAFControl_Reader",
    "OCP.STEPCAFControl.STEPCAFControl_Reader.SetColorMode",
    "OCP.STEPCAFControl.STEPCAFControl_Reader.SetNameMode",
    "OCP.STEPCAFControl.STEPCAFControl_Reader.SetLayerMode",
    "OCP.STEPCAFControl.STEPCAFControl_Reader.SetPropsMode",
    "OCP.STEPCAFControl.STEPCAFControl_Reader.ReadFile",
    "OCP.STEPCAFControl.STEPCAFControl_Reader.Transfer",
    "OCP.STEPCAFControl.STEPCAFControl_Reader.Reader",
    "OCP.STEPCAFControl.STEPCAFControl_Reader.ChangeReader",
    "OCP.IGESCAFControl.IGESCAFControl_Reader",
    "OCP.IGESCAFControl.IGESCAFControl_Reader.SetColorMode",
    "OCP.IGESCAFControl.IGESCAFControl_Reader.SetNameMode",
    "OCP.IGESCAFControl.IGESCAFControl_Reader.SetLayerMode",
    "OCP.IGESCAFControl.IGESCAFControl_Reader.SetPropsMode",
    "OCP.IGESCAFControl.IGESCAFControl_Reader.ReadFile",
    "OCP.IGESCAFControl.IGESCAFControl_Reader.Transfer",
    "OCP.IGESCAFControl.IGESCAFControl_Reader.Reader",
    "OCP.IGESCAFControl.IGESCAFControl_Reader.ChangeReader",
    "OCP.IFSelect.IFSelect_ReturnStatus",
    "OCP.IFSelect.IFSelect_RetDone",
    "OCP.XSControl.XSControl_Reader.PrintCheckLoad",
    "OCP.XSControl.XSControl_Reader.PrintCheckTransfer",
    "OCP.XSControl.XSControl_Reader.GetStatsTransfer",
    "OCP.STEPControl.STEPControl_Reader.FileUnits",
    "OCP.STEPControl.STEPControl_Reader.SystemLengthUnit",
    "OCP.STEPControl.STEPControl_Reader.SetSystemLengthUnit",
    "OCP.IGESControl.IGESControl_Reader.IGESModel",
    "OCP.IGESControl.IGESControl_Reader.SystemLengthUnit",
    "OCP.IGESControl.IGESControl_Reader.SetSystemLengthUnit",
    "OCP.STEPCAFControl.STEPCAFControl_Reader.ExternFiles",
    "OCP.STEPCAFControl.STEPCAFControl_Reader.ExternFile",
    "OCP.TDF.TDF_Label",
    "OCP.TDF.TDF_LabelSequence",
    "OCP.TDF.TDF_Tool",
    "OCP.TDF.TDF_LabelSequence.Length",
    "OCP.TDF.TDF_LabelSequence.Value",
    "OCP.TDF.TDF_LabelSequence.Append",
    "OCP.TDF.TDF_Tool.Entry_s",
    "OCP.XCAFDoc.XCAFDoc_ShapeTool",
    "OCP.XCAFDoc.XCAFDoc_ShapeTool.GetFreeShapes",
    "OCP.XCAFDoc.XCAFDoc_ShapeTool.GetComponents",
    "OCP.XCAFDoc.XCAFDoc_ShapeTool.GetUsers",
    "OCP.XCAFDoc.XCAFDoc_ShapeTool.GetSubShapes",
    "OCP.XCAFDoc.XCAFDoc_ShapeTool.GetReferredShape",
    "OCP.XCAFDoc.XCAFDoc_ShapeTool.GetLocation",
    "OCP.XCAFDoc.XCAFDoc_ShapeTool.GetShape",
    "OCP.XCAFDoc.XCAFDoc_ShapeTool.IsAssembly",
    "OCP.XCAFDoc.XCAFDoc_ShapeTool.IsComponent",
    "OCP.XCAFDoc.XCAFDoc_ShapeTool.IsReference",
    "OCP.XCAFDoc.XCAFDoc_ColorTool",
    "OCP.XCAFDoc.XCAFDoc_ColorTool.GetColor",
    "OCP.XCAFDoc.XCAFDoc_ColorTool.GetColors",
    "OCP.XCAFDoc.XCAFDoc_ColorTool.IsSet",
    "OCP.XCAFDoc.XCAFDoc_ColorTool.IsVisible",
    "OCP.XCAFDoc.XCAFDoc_LayerTool",
    "OCP.XCAFDoc.XCAFDoc_LayerTool.GetLayers",
    "OCP.XCAFDoc.XCAFDoc_LayerTool.GetLayer",
    "OCP.XCAFDoc.XCAFDoc_LayerTool.IsSet",
    "OCP.XCAFDoc.XCAFDoc_LayerTool.IsVisible",
    "OCP.TDataStd.TDataStd_Name.GetID_s",
    "OCP.TDF.TDF_Label.FindAttribute",
    "OCP.TopExp.TopExp.MapShapes_s",
    "OCP.TopExp.TopExp_Explorer",
    "OCP.TopExp.TopExp_Explorer.More",
    "OCP.TopExp.TopExp_Explorer.Next",
    "OCP.TopExp.TopExp_Explorer.Current",
    "OCP.TopTools.TopTools_IndexedMapOfShape",
    "OCP.TopTools.TopTools_IndexedMapOfShape.Extent",
    "OCP.TopTools.TopTools_IndexedMapOfShape.FindKey",
    "OCP.TopTools.TopTools_IndexedMapOfShape.Add",
    "OCP.TopLoc.TopLoc_Location.Transformation",
    "OCP.gp.gp_Trsf",
    "OCP.gp.gp_Trsf.Value",
    "OCP.gp.gp_Trsf.TranslationPart",
    "OCP.gp.gp_Trsf.VectorialPart",
    "OCP.gp.gp_Trsf.IsNegative",
    "OCP.gp.gp_Trsf.Inverted",
    "OCP.gp.gp_Trsf.Multiplied",
    "OCP.gp.gp_Trsf.Multiply",
    "OCP.gp.gp_Trsf.PreMultiply",
    "OCP.gp.gp_Trsf.Form",
    "OCP.gp.gp_Trsf.ScaleFactor",
    "OCP.Interface.Interface_Static.IsPresent_s",
    "OCP.Interface.Interface_Static.CVal_s",
    "OCP.Interface.Interface_Static.IVal_s",
    "OCP.Interface.Interface_Static.RVal_s",
    "OCP.Interface.Interface_Static.SetCVal_s",
    "OCP.Interface.Interface_Static.SetIVal_s",
    "OCP.Interface.Interface_Static.SetRVal_s",
)
VERSION_TARGET = "OCP.Standard.Standard_Version_Complete_s"
CANDIDATE_SETTING_KEYS = (
    "read.precision.mode",
    "read.precision.val",
    "read.step.product.mode",
    "read.step.assembly.level",
    "xstep.cascade.unit",
    "write.step.unit",
    "write.step.schema",
    "read.iges.onlyvisible",
    "write.iges.unit",
)


class Blocked(RuntimeError):
    """First fail-closed evidence outcome."""

    def __init__(self, stage: str, message: str):
        super().__init__(message)
        self.stage = stage
        self.message = message


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="microseconds")


def check_deadline(deadline: float | None, stage: str) -> None:
    if deadline is not None and time.monotonic() >= deadline:
        raise Blocked("resource", f"{stage} exceeded the global deadline")


def bounded_wait_milliseconds(deadline: float, maximum: int, stage: str) -> int:
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise Blocked("resource", f"{stage} deadline exceeded")
    return max(1, min(maximum, math.ceil(remaining * 1000.0)))


def sha256_file(
    path: Path,
    *,
    cap: int | None = None,
    deadline: float | None = None,
) -> tuple[str, int]:
    digest = hashlib.sha256()
    total = 0
    with path.open("rb") as stream:
        while True:
            check_deadline(deadline, "hashing")
            chunk = stream.read(HASH_CHUNK)
            if not chunk:
                break
            total += len(chunk)
            if cap is not None and total > cap:
                raise Blocked("resource", f"{path.name} exceeds {cap} bytes")
            digest.update(chunk)
    return digest.hexdigest(), total


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def b64_sha256(data: bytes) -> str:
    return base64.urlsafe_b64encode(hashlib.sha256(data).digest()).rstrip(b"=").decode("ascii")


def canonical_json_bytes(value: object) -> bytes:
    data = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8") + b"\n"
    if len(data) > MAX_JSON_BYTES:
        raise Blocked("resource", f"JSON output exceeds {MAX_JSON_BYTES} bytes")
    return data


def json_depth(value: object, depth: int = 0) -> int:
    if depth > MAX_JSON_DEPTH:
        raise Blocked("validation", f"JSON nesting exceeds {MAX_JSON_DEPTH}")
    if isinstance(value, dict):
        return max([depth] + [json_depth(item, depth + 1) for item in value.values()])
    if isinstance(value, list):
        return max([depth] + [json_depth(item, depth + 1) for item in value])
    return depth


def load_canonical_json(path: Path) -> object:
    data = path.read_bytes()
    if len(data) > MAX_JSON_BYTES:
        raise Blocked("validation", f"{path.name} exceeds JSON cap")
    try:
        value = json.loads(data)
    except Exception as exc:
        raise Blocked("validation", f"invalid JSON {path.name}: {exc}") from exc
    json_depth(value)
    if canonical_json_bytes(value) != data:
        raise Blocked("validation", f"non-canonical JSON: {path.name}")
    return value


def task_tree_bytes() -> int:
    if not TASK_ROOT.exists():
        return 0
    total = 0
    for root, dirs, files in os.walk(TASK_ROOT, followlinks=False):
        root_path = Path(root)
        for name in dirs:
            entry = root_path / name
            if entry.is_symlink() or entry.is_junction():
                raise Blocked("resource", f"task tree contains link: {entry}")
        for name in files:
            entry = root_path / name
            if entry.is_symlink():
                raise Blocked("resource", f"task tree contains link: {entry}")
            try:
                total += entry.stat().st_size
            except FileNotFoundError:
                # Venv/pip may atomically replace their own task-root files.  A
                # fresh bounded scan occurs at the next 250 ms checkpoint.
                continue
            if total > MAX_TASK_BYTES:
                raise Blocked("resource", f"task tree exceeds {MAX_TASK_BYTES} bytes")
    return total


def safe_zip_name(name: str) -> PurePosixPath:
    if not name or "\\" in name or "\x00" in name or ":" in name:
        raise Blocked("wheel", f"unsafe archive path: {name!r}")
    path = PurePosixPath(name)
    if (
        path.is_absolute()
        or path.as_posix() != name
        or any(part in ("", ".", "..") for part in path.parts)
    ):
        raise Blocked("wheel", f"unsafe archive path: {name!r}")
    return path


def decode_record_hash(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise Blocked("wheel", f"invalid RECORD hash {value!r}")
    algorithm, encoded = value.split("=", 1)
    if algorithm != "sha256" or not encoded:
        raise Blocked("wheel", f"non-sha256 RECORD hash {value!r}")
    return algorithm, encoded


def read_zip_limited(archive: zipfile.ZipFile, info: zipfile.ZipInfo, cap: int) -> bytes:
    if info.file_size > cap:
        raise Blocked("wheel", f"{info.filename} exceeds {cap} bytes")
    out = bytearray()
    with archive.open(info, "r") as stream:
        while True:
            chunk = stream.read(min(HASH_CHUNK, cap + 1 - len(out)))
            if not chunk:
                break
            out.extend(chunk)
            if len(out) > cap:
                raise Blocked("wheel", f"{info.filename} exceeds {cap} bytes")
    if len(out) != info.file_size:
        raise Blocked("wheel", f"size mismatch while reading {info.filename}")
    return bytes(out)


def raw_headers(message_bytes: bytes) -> list[list[str]]:
    message = email.parser.BytesParser().parsebytes(message_bytes)
    return [[name, value] for name, value in message.raw_items()]


def message_values(message_bytes: bytes, key: str) -> list[str]:
    message = email.parser.BytesParser().parsebytes(message_bytes)
    return list(message.get_all(key, []))


def validate_wheel(
    spec: dict[str, object],
    path: Path,
    global_deadline: float,
) -> dict[str, object]:
    actual_hash, actual_size = sha256_file(
        path,
        cap=int(spec["bytes"]),
        deadline=global_deadline,
    )
    if actual_size != spec["bytes"] or actual_hash != spec["sha256"]:
        raise Blocked("wheel", f"frozen size/hash mismatch for {path.name}")
    if path.name != spec["filename"]:
        raise Blocked("wheel", f"filename mismatch: {path.name}")

    with zipfile.ZipFile(path, "r") as archive:
        infos = archive.infolist()
        if len(infos) > MAX_WHEEL_MEMBERS:
            raise Blocked("wheel", f"member count exceeds {MAX_WHEEL_MEMBERS}")
        names: dict[str, zipfile.ZipInfo] = {}
        directories: list[dict[str, object]] = []
        directory_attribute_counts: dict[tuple[int, int, int, int], int] = {}
        file_attribute_counts: dict[tuple[int, int, int, int], int] = {}
        logical_names: set[str] = set()
        folded: set[str] = set()
        expanded = 0
        for info in infos:
            check_deadline(global_deadline, "wheel inventory")
            is_directory = info.is_dir()
            if is_directory:
                if not info.filename.endswith("/") or info.filename.endswith("//"):
                    raise Blocked("wheel", f"invalid explicit directory name: {info.filename!r}")
                logical_name = info.filename[:-1]
            else:
                if info.filename.endswith("/"):
                    raise Blocked("wheel", f"directory-like file member: {info.filename!r}")
                logical_name = info.filename
            safe_zip_name(logical_name)
            mode = (info.external_attr >> 16) & 0xFFFF
            if stat.S_ISLNK(mode):
                raise Blocked("wheel", f"symlink member: {info.filename}")
            key = logical_name.casefold()
            if logical_name in logical_names or key in folded:
                raise Blocked("wheel", f"duplicate/colliding member: {info.filename}")
            logical_names.add(logical_name)
            folded.add(key)
            expanded += info.file_size
            if expanded > MAX_TASK_BYTES:
                raise Blocked("wheel", "wheel expanded bytes exceed task cap")
            if is_directory:
                directory_key = (
                    info.create_system,
                    info.external_attr,
                    info.flag_bits,
                    info.compress_type,
                )
                expected_directory_keys = {
                    tuple(item[:4]) for item in spec["directory_attribute_counts"]
                }
                if (
                    not stat.S_ISDIR(mode)
                    or directory_key not in expected_directory_keys
                    or (info.external_attr & 0xFFFF) not in (0, 0x10)
                    or info.file_size != 0
                    or info.compress_size != 0
                    or info.CRC != 0
                    or read_zip_limited(archive, info, 0) != b""
                ):
                    raise Blocked("wheel", f"unsafe explicit directory member: {info.filename}")
                directory_attribute_counts[directory_key] = (
                    directory_attribute_counts.get(directory_key, 0) + 1
                )
                directories.append(
                    {
                        "name": info.filename,
                        "create_system": info.create_system,
                        "external_attr": info.external_attr,
                        "flag_bits": info.flag_bits,
                        "compress_type": info.compress_type,
                        "file_size": info.file_size,
                        "compress_size": info.compress_size,
                        "crc": info.CRC,
                    }
                )
                continue
            file_key = (
                info.create_system,
                info.external_attr,
                info.flag_bits,
                info.compress_type,
            )
            expected_file_keys = {tuple(item[:4]) for item in spec["file_attribute_counts"]}
            if not stat.S_ISREG(mode) or file_key not in expected_file_keys:
                raise Blocked("wheel", f"nonregular/unexpected file attributes: {info.filename}")
            file_attribute_counts[file_key] = file_attribute_counts.get(file_key, 0) + 1
            names[info.filename] = info

        if (
            len(infos) != spec["member_count"]
            or len(names) != spec["file_member_count"]
            or len(directories) != spec["directory_count"]
            or sorted((*key, count) for key, count in directory_attribute_counts.items())
            != sorted(spec["directory_attribute_counts"])
            or sorted((*key, count) for key, count in file_attribute_counts.items())
            != sorted(spec["file_attribute_counts"])
        ):
            raise Blocked(
                "wheel",
                "frozen member/file/directory count mismatch for " + path.name,
            )

        prefix = str(spec["name"]).replace("-", "_") + "-" + str(spec["version"])
        dist_info = prefix + ".dist-info"
        metadata_name = dist_info + "/METADATA"
        wheel_name = dist_info + "/WHEEL"
        record_name = dist_info + "/RECORD"
        for required in (metadata_name, wheel_name, record_name):
            if required not in names:
                raise Blocked("wheel", f"missing exact {required}")
        if sum(name.endswith(".dist-info/METADATA") for name in names) != 1:
            raise Blocked("wheel", "wheel does not have exactly one METADATA")
        if sum(name.endswith(".dist-info/WHEEL") for name in names) != 1:
            raise Blocked("wheel", "wheel does not have exactly one WHEEL")
        if sum(name.endswith(".dist-info/RECORD") for name in names) != 1:
            raise Blocked("wheel", "wheel does not have exactly one RECORD")

        metadata = read_zip_limited(archive, names[metadata_name], MIB)
        wheel_data = read_zip_limited(archive, names[wheel_name], MIB)
        record_data = read_zip_limited(archive, names[record_name], MAX_JSON_BYTES)
        if message_values(metadata, "Name") != [spec["name"]]:
            raise Blocked("wheel", f"Name mismatch for {path.name}")
        if message_values(metadata, "Version") != [spec["version"]]:
            raise Blocked("wheel", f"Version mismatch for {path.name}")
        if message_values(metadata, "Requires-Python") != [spec["requires_python"]]:
            raise Blocked("wheel", f"Requires-Python mismatch for {path.name}")
        if tuple(message_values(metadata, "Requires-Dist")) != spec["requires_dist"]:
            raise Blocked("wheel", f"Requires-Dist mismatch for {path.name}")
        if message_values(wheel_data, "Tag") != [spec["tag"]]:
            raise Blocked("wheel", f"Tag mismatch for {path.name}")
        root_values = message_values(wheel_data, "Root-Is-Purelib")
        if len(root_values) != 1 or root_values[0] not in ("true", "false"):
            raise Blocked("wheel", f"invalid Root-Is-Purelib for {path.name}")

        try:
            record_text = record_data.decode("utf-8")
            rows = list(csv.reader(io.StringIO(record_text, newline="")))
        except Exception as exc:
            raise Blocked("wheel", f"invalid RECORD encoding/CSV: {exc}") from exc
        record_map: dict[str, tuple[str, str]] = {}
        for row in rows:
            check_deadline(global_deadline, "wheel RECORD inventory")
            if len(row) != 3:
                raise Blocked("wheel", f"RECORD row arity is {len(row)}")
            member, hash_value, size_value = row
            safe_zip_name(member)
            if member in record_map or member.casefold() in {item.casefold() for item in record_map}:
                raise Blocked("wheel", f"duplicate RECORD row {member}")
            record_map[member] = (hash_value, size_value)
        if set(record_map) != set(names):
            missing = sorted(set(names) - set(record_map))
            extra = sorted(set(record_map) - set(names))
            raise Blocked("wheel", f"RECORD/member mismatch missing={missing[:3]} extra={extra[:3]}")
        for member, info in names.items():
            check_deadline(global_deadline, "wheel RECORD verification")
            hash_value, size_value = record_map[member]
            if member == record_name:
                if hash_value or size_value:
                    raise Blocked("wheel", "RECORD self-row must have empty hash and size")
                continue
            _, encoded = decode_record_hash(hash_value)
            if size_value != str(info.file_size):
                raise Blocked("wheel", f"RECORD size mismatch for {member}")
            digest = hashlib.sha256()
            count = 0
            with archive.open(info, "r") as stream:
                while True:
                    chunk = stream.read(HASH_CHUNK)
                    if not chunk:
                        break
                    digest.update(chunk)
                    count += len(chunk)
            actual_encoded = base64.urlsafe_b64encode(digest.digest()).rstrip(b"=").decode("ascii")
            if count != info.file_size or actual_encoded != encoded:
                raise Blocked("wheel", f"RECORD payload mismatch for {member}")

        return {
            "status": "VERIFIED",
            "filename": path.name,
            "original_url": spec["url"],
            "source_path": str((V2_WHEELHOUSE / path.name).resolve()),
            "bytes": actual_size,
            "sha256": actual_hash,
            "tag": spec["tag"],
            "pep658_metadata_sha256": spec.get("pep658_sha256"),
            "expanded_bytes": expanded,
            "member_count": len(infos),
            "file_member_count": len(names),
            "directory_count": len(directories),
            "directories": directories,
            "file_attribute_counts": [
                [*key, count] for key, count in sorted(file_attribute_counts.items())
            ],
            "directory_attribute_counts": [
                [*key, count] for key, count in sorted(directory_attribute_counts.items())
            ],
            "dist_info": dist_info,
            "metadata": {
                "bytes": len(metadata),
                "sha256": sha256_bytes(metadata),
                "raw_base64": base64.b64encode(metadata).decode("ascii"),
                "headers": raw_headers(metadata),
            },
            "wheel": {
                "bytes": len(wheel_data),
                "sha256": sha256_bytes(wheel_data),
                "raw_base64": base64.b64encode(wheel_data).decode("ascii"),
                "headers": raw_headers(wheel_data),
            },
            "record": {
                "bytes": len(record_data),
                "sha256": sha256_bytes(record_data),
                "rows": [[name, *record_map[name]] for name in record_map],
            },
        }


# Windows Job Object and suspended-process definitions.  They are referenced
# only by controller mode after the host preflight proves Windows AMD64.
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True) if os.name == "nt" else None


class LARGE_INTEGER(ctypes.Structure):
    _fields_ = [("QuadPart", ctypes.c_longlong)]


class IO_COUNTERS(ctypes.Structure):
    _fields_ = [
        ("ReadOperationCount", ctypes.c_ulonglong),
        ("WriteOperationCount", ctypes.c_ulonglong),
        ("OtherOperationCount", ctypes.c_ulonglong),
        ("ReadTransferCount", ctypes.c_ulonglong),
        ("WriteTransferCount", ctypes.c_ulonglong),
        ("OtherTransferCount", ctypes.c_ulonglong),
    ]


class JOBOBJECT_BASIC_LIMIT_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("PerProcessUserTimeLimit", LARGE_INTEGER),
        ("PerJobUserTimeLimit", LARGE_INTEGER),
        ("LimitFlags", wintypes.DWORD),
        ("MinimumWorkingSetSize", ctypes.c_size_t),
        ("MaximumWorkingSetSize", ctypes.c_size_t),
        ("ActiveProcessLimit", wintypes.DWORD),
        ("Affinity", ctypes.c_size_t),
        ("PriorityClass", wintypes.DWORD),
        ("SchedulingClass", wintypes.DWORD),
    ]


class JOBOBJECT_EXTENDED_LIMIT_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("BasicLimitInformation", JOBOBJECT_BASIC_LIMIT_INFORMATION),
        ("IoInfo", IO_COUNTERS),
        ("ProcessMemoryLimit", ctypes.c_size_t),
        ("JobMemoryLimit", ctypes.c_size_t),
        ("PeakProcessMemoryUsed", ctypes.c_size_t),
        ("PeakJobMemoryUsed", ctypes.c_size_t),
    ]


class JOBOBJECT_BASIC_ACCOUNTING_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("TotalUserTime", LARGE_INTEGER),
        ("TotalKernelTime", LARGE_INTEGER),
        ("ThisPeriodTotalUserTime", LARGE_INTEGER),
        ("ThisPeriodTotalKernelTime", LARGE_INTEGER),
        ("TotalPageFaultCount", wintypes.DWORD),
        ("TotalProcesses", wintypes.DWORD),
        ("ActiveProcesses", wintypes.DWORD),
        ("TotalTerminatedProcesses", wintypes.DWORD),
    ]


class SECURITY_ATTRIBUTES(ctypes.Structure):
    _fields_ = [
        ("nLength", wintypes.DWORD),
        ("lpSecurityDescriptor", wintypes.LPVOID),
        ("bInheritHandle", wintypes.BOOL),
    ]


class STARTUPINFOW(ctypes.Structure):
    _fields_ = [
        ("cb", wintypes.DWORD),
        ("lpReserved", wintypes.LPWSTR),
        ("lpDesktop", wintypes.LPWSTR),
        ("lpTitle", wintypes.LPWSTR),
        ("dwX", wintypes.DWORD),
        ("dwY", wintypes.DWORD),
        ("dwXSize", wintypes.DWORD),
        ("dwYSize", wintypes.DWORD),
        ("dwXCountChars", wintypes.DWORD),
        ("dwYCountChars", wintypes.DWORD),
        ("dwFillAttribute", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("wShowWindow", wintypes.WORD),
        ("cbReserved2", wintypes.WORD),
        ("lpReserved2", ctypes.POINTER(ctypes.c_byte)),
        ("hStdInput", wintypes.HANDLE),
        ("hStdOutput", wintypes.HANDLE),
        ("hStdError", wintypes.HANDLE),
    ]


class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("hProcess", wintypes.HANDLE),
        ("hThread", wintypes.HANDLE),
        ("dwProcessId", wintypes.DWORD),
        ("dwThreadId", wintypes.DWORD),
    ]


if kernel32 is not None:
    kernel32.CreateJobObjectW.argtypes = [ctypes.POINTER(SECURITY_ATTRIBUTES), wintypes.LPCWSTR]
    kernel32.CreateJobObjectW.restype = wintypes.HANDLE
    kernel32.SetInformationJobObject.argtypes = [
        wintypes.HANDLE,
        ctypes.c_int,
        wintypes.LPVOID,
        wintypes.DWORD,
    ]
    kernel32.SetInformationJobObject.restype = wintypes.BOOL
    kernel32.QueryInformationJobObject.argtypes = [
        wintypes.HANDLE,
        ctypes.c_int,
        wintypes.LPVOID,
        wintypes.DWORD,
        ctypes.POINTER(wintypes.DWORD),
    ]
    kernel32.QueryInformationJobObject.restype = wintypes.BOOL
    kernel32.AssignProcessToJobObject.argtypes = [wintypes.HANDLE, wintypes.HANDLE]
    kernel32.AssignProcessToJobObject.restype = wintypes.BOOL
    kernel32.IsProcessInJob.argtypes = [
        wintypes.HANDLE,
        wintypes.HANDLE,
        ctypes.POINTER(wintypes.BOOL),
    ]
    kernel32.IsProcessInJob.restype = wintypes.BOOL
    kernel32.CreatePipe.argtypes = [
        ctypes.POINTER(wintypes.HANDLE),
        ctypes.POINTER(wintypes.HANDLE),
        ctypes.POINTER(SECURITY_ATTRIBUTES),
        wintypes.DWORD,
    ]
    kernel32.CreatePipe.restype = wintypes.BOOL
    kernel32.SetHandleInformation.argtypes = [wintypes.HANDLE, wintypes.DWORD, wintypes.DWORD]
    kernel32.SetHandleInformation.restype = wintypes.BOOL
    kernel32.CreateFileW.argtypes = [
        wintypes.LPCWSTR,
        wintypes.DWORD,
        wintypes.DWORD,
        ctypes.POINTER(SECURITY_ATTRIBUTES),
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.HANDLE,
    ]
    kernel32.CreateFileW.restype = wintypes.HANDLE
    kernel32.CreateProcessW.argtypes = [
        wintypes.LPCWSTR,
        wintypes.LPWSTR,
        wintypes.LPVOID,
        wintypes.LPVOID,
        wintypes.BOOL,
        wintypes.DWORD,
        wintypes.LPVOID,
        wintypes.LPCWSTR,
        ctypes.POINTER(STARTUPINFOW),
        ctypes.POINTER(PROCESS_INFORMATION),
    ]
    kernel32.CreateProcessW.restype = wintypes.BOOL
    kernel32.TerminateProcess.argtypes = [wintypes.HANDLE, wintypes.UINT]
    kernel32.TerminateProcess.restype = wintypes.BOOL
    kernel32.ResumeThread.argtypes = [wintypes.HANDLE]
    kernel32.ResumeThread.restype = wintypes.DWORD
    kernel32.WaitForSingleObject.argtypes = [wintypes.HANDLE, wintypes.DWORD]
    kernel32.WaitForSingleObject.restype = wintypes.DWORD
    kernel32.TerminateJobObject.argtypes = [wintypes.HANDLE, wintypes.UINT]
    kernel32.TerminateJobObject.restype = wintypes.BOOL
    kernel32.GetExitCodeProcess.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
    kernel32.GetExitCodeProcess.restype = wintypes.BOOL
    kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
    kernel32.CloseHandle.restype = wintypes.BOOL
    kernel32.MoveFileExW.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.DWORD]
    kernel32.MoveFileExW.restype = wintypes.BOOL
JOB_OBJECT_LIMIT_ACTIVE_PROCESS = 0x00000008
JOB_OBJECT_LIMIT_PROCESS_MEMORY = 0x00000100
JOB_OBJECT_LIMIT_JOB_MEMORY = 0x00000200
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 0x00002000
CREATE_SUSPENDED = 0x00000004
CREATE_BREAKAWAY_FROM_JOB = 0x01000000
CREATE_NO_WINDOW = 0x08000000
CREATE_UNICODE_ENVIRONMENT = 0x00000400
STARTF_USESTDHANDLES = 0x00000100
HANDLE_FLAG_INHERIT = 0x00000001
WAIT_OBJECT_0 = 0
WAIT_TIMEOUT = 258
INFINITE = 0xFFFFFFFF
JobObjectExtendedLimitInformation = 9
JobObjectBasicAccountingInformation = 1
MOVEFILE_WRITE_THROUGH = 0x00000008
INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value
_FROZEN_PROBE_SHA256 = None


def win_error(label: str) -> Blocked:
    return Blocked("resource", f"{label}: Windows error {ctypes.get_last_error()}")


def configure_worker_job():
    assert kernel32 is not None
    handle = kernel32.CreateJobObjectW(None, None)
    if not handle:
        raise win_error("CreateJobObjectW")
    info = JOBOBJECT_EXTENDED_LIMIT_INFORMATION()
    flags = (
        JOB_OBJECT_LIMIT_ACTIVE_PROCESS
        | JOB_OBJECT_LIMIT_PROCESS_MEMORY
        | JOB_OBJECT_LIMIT_JOB_MEMORY
        | JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
    )
    info.BasicLimitInformation.LimitFlags = flags
    info.BasicLimitInformation.ActiveProcessLimit = WORKER_ACTIVE_PROCESS_LIMIT
    info.ProcessMemoryLimit = WORKER_PROCESS_MEMORY_BYTES
    info.JobMemoryLimit = WORKER_JOB_MEMORY_BYTES
    if not kernel32.SetInformationJobObject(
        handle,
        JobObjectExtendedLimitInformation,
        ctypes.byref(info),
        ctypes.sizeof(info),
    ):
        kernel32.CloseHandle(handle)
        raise win_error("SetInformationJobObject")
    return handle


def active_job_processes(job) -> int:
    assert kernel32 is not None
    accounting = JOBOBJECT_BASIC_ACCOUNTING_INFORMATION()
    returned = wintypes.DWORD()
    if not kernel32.QueryInformationJobObject(
        job,
        JobObjectBasicAccountingInformation,
        ctypes.byref(accounting),
        ctypes.sizeof(accounting),
        ctypes.byref(returned),
    ):
        raise win_error("QueryInformationJobObject")
    return int(accounting.ActiveProcesses)


def environment_block(environment: dict[str, str]):
    items = sorted(environment.items(), key=lambda item: item[0].upper())
    text = "\0".join(f"{key}={value}" for key, value in items) + "\0\0"
    return ctypes.create_unicode_buffer(text)


def read_pipe(
    handle,
    limit: int,
    result: dict[str, object],
    key: str,
    overflow_event: threading.Event,
) -> None:
    import msvcrt

    raw_handle = handle.value if hasattr(handle, "value") else int(handle)
    if raw_handle in (None, 0, ctypes.c_void_p(-1).value):
        result[key + "_reader_error"] = "invalid pipe handle"
        overflow_event.set()
        return
    try:
        fd = msvcrt.open_osfhandle(int(raw_handle), os.O_RDONLY)
    except BaseException as exc:
        result[key + "_reader_error"] = repr(exc)
        if kernel32 is None or not kernel32.CloseHandle(handle):
            result[key + "_reader_cleanup_error"] = (
                "CloseHandle after open_osfhandle failure: Windows error "
                f"{ctypes.get_last_error()}"
            )
        overflow_event.set()
        return
    data = bytearray()
    overflow = False
    try:
        stream = os.fdopen(fd, "rb", closefd=True)
    except BaseException as exc:
        result[key + "_reader_error"] = repr(exc)
        try:
            os.close(fd)
        except BaseException as cleanup:
            result[key + "_reader_cleanup_error"] = repr(cleanup)
        overflow_event.set()
        return
    try:
        with stream:
            while True:
                remaining = limit - len(data)
                chunk = stream.read(min(65536, remaining + 1))
                if not chunk:
                    break
                if len(chunk) > remaining:
                    data.extend(chunk[:remaining])
                    overflow = True
                    overflow_event.set()
                    break
                data.extend(chunk)
    except BaseException as exc:
        result[key + "_reader_error"] = repr(exc)
        overflow_event.set()
    result[key] = bytes(data)
    result[key + "_overflow"] = overflow


def wait_for_job_zero(worker_job, deadline: float, stage: str) -> None:
    while True:
        if time.monotonic() >= deadline:
            raise Blocked("resource", f"{stage} worker tree did not quiesce")
        if active_job_processes(worker_job) == 0:
            check_deadline(deadline, stage)
            return
        time.sleep(min(JOB_POLL_SECONDS, max(0.0, deadline - time.monotonic())))


def terminate_job_and_confirm_empty(
    worker_job,
    exit_code: int,
    stage: str,
    global_deadline: float,
) -> None:
    assert kernel32 is not None
    try:
        active = active_job_processes(worker_job)
    except BaseException as observation_error:
        if not kernel32.TerminateJobObject(worker_job, exit_code):
            observation_error.add_note(
                f"TerminateJobObject({stage}) also failed with Windows error "
                f"{ctypes.get_last_error()}"
            )
        else:
            deadline = min(
                global_deadline,
                time.monotonic() + ACTIVE_PROCESS_ZERO_GRACE_SECONDS,
            )
            try:
                wait_for_job_zero(worker_job, deadline, stage)
            except BaseException as confirmation_error:
                observation_error.add_note(
                    "post-termination zero confirmation also failed: "
                    f"{type(confirmation_error).__name__}: {confirmation_error}"
                )
        raise
    if not active:
        return
    if not kernel32.TerminateJobObject(worker_job, exit_code):
        raise win_error(f"TerminateJobObject({stage})")
    deadline = min(global_deadline, time.monotonic() + ACTIVE_PROCESS_ZERO_GRACE_SECONDS)
    wait_for_job_zero(worker_job, deadline, stage)


def run_worker(
    worker_job,
    argv: list[str],
    *,
    cwd: Path,
    environment: dict[str, str],
    stage: str,
    seconds: float,
    global_deadline: float,
) -> tuple[int, bytes, bytes]:
    assert kernel32 is not None
    check_deadline(global_deadline, stage)
    if active_job_processes(worker_job) != 0:
        raise Blocked("resource", f"{stage} worker job was not empty before launch")
    if _FROZEN_PROBE_SHA256 and sha256_file(TASK_ROOT / "probe.py")[0] != _FROZEN_PROBE_SHA256:
        raise Blocked("identity", f"probe changed immediately before {stage} child")
    task_tree_bytes()
    deadline = min(global_deadline, time.monotonic() + seconds)
    if time.monotonic() >= deadline:
        raise Blocked("resource", f"{stage} deadline elapsed before launch")
    sa = SECURITY_ATTRIBUTES(ctypes.sizeof(SECURITY_ATTRIBUTES), None, True)
    out_read = wintypes.HANDLE()
    out_write = wintypes.HANDLE()
    err_read = wintypes.HANDLE()
    err_write = wintypes.HANDLE()
    if not kernel32.CreatePipe(ctypes.byref(out_read), ctypes.byref(out_write), ctypes.byref(sa), 0):
        raise win_error("CreatePipe(stdout)")
    if not kernel32.CreatePipe(ctypes.byref(err_read), ctypes.byref(err_write), ctypes.byref(sa), 0):
        kernel32.CloseHandle(out_read)
        kernel32.CloseHandle(out_write)
        raise win_error("CreatePipe(stderr)")
    if not kernel32.SetHandleInformation(out_read, HANDLE_FLAG_INHERIT, 0):
        for handle in (out_read, out_write, err_read, err_write):
            kernel32.CloseHandle(handle)
        raise win_error("SetHandleInformation(stdout)")
    if not kernel32.SetHandleInformation(err_read, HANDLE_FLAG_INHERIT, 0):
        for handle in (out_read, out_write, err_read, err_write):
            kernel32.CloseHandle(handle)
        raise win_error("SetHandleInformation(stderr)")
    null_input = kernel32.CreateFileW(
        "NUL", 0x80000000, 0x00000001 | 0x00000002, ctypes.byref(sa), 3, 0x80, None
    )
    invalid_handle = ctypes.c_void_p(-1).value
    if null_input in (None, 0, invalid_handle):
        for handle in (out_read, out_write, err_read, err_write):
            kernel32.CloseHandle(handle)
        raise win_error("CreateFileW(NUL)")
    startup = STARTUPINFOW()
    startup.cb = ctypes.sizeof(startup)
    startup.dwFlags = STARTF_USESTDHANDLES
    startup.hStdInput = null_input
    startup.hStdOutput = out_write
    startup.hStdError = err_write
    process = PROCESS_INFORMATION()
    command = ctypes.create_unicode_buffer(subprocess.list2cmdline(argv))
    env_block = environment_block(environment)
    flags = CREATE_SUSPENDED | CREATE_BREAKAWAY_FROM_JOB | CREATE_NO_WINDOW | CREATE_UNICODE_ENVIRONMENT
    created = kernel32.CreateProcessW(
        None,
        command,
        None,
        None,
        True,
        flags,
        env_block,
        str(cwd),
        ctypes.byref(startup),
        ctypes.byref(process),
    )
    kernel32.CloseHandle(out_write)
    kernel32.CloseHandle(err_write)
    kernel32.CloseHandle(null_input)
    if not created:
        kernel32.CloseHandle(out_read)
        kernel32.CloseHandle(err_read)
        raise win_error(f"CreateProcessW({stage})")
    assigned = False
    threads: list[threading.Thread] = []
    started_threads: list[threading.Thread] = []
    result: dict[str, object] = {}
    overflow_event = threading.Event()
    try:
        if not kernel32.AssignProcessToJobObject(worker_job, process.hProcess):
            if not kernel32.TerminateProcess(process.hProcess, 120):
                raise win_error(f"TerminateProcess(unassigned {stage})")
            wait_ms = bounded_wait_milliseconds(global_deadline, 10000, stage)
            if kernel32.WaitForSingleObject(process.hProcess, wait_ms) != WAIT_OBJECT_0:
                raise Blocked("resource", f"{stage} unassigned process did not exit")
            raise win_error(f"AssignProcessToJobObject({stage})")
        assigned = True
        in_job = wintypes.BOOL()
        if not kernel32.IsProcessInJob(process.hProcess, worker_job, ctypes.byref(in_job)):
            terminate_job_and_confirm_empty(worker_job, 121, stage, global_deadline)
            raise win_error(f"IsProcessInJob({stage})")
        if not in_job.value:
            terminate_job_and_confirm_empty(worker_job, 121, stage, global_deadline)
            raise Blocked("resource", f"{stage} root was not contained by the worker job")
        threads = [
            threading.Thread(
                target=read_pipe,
                args=(out_read, MAX_STREAM_BYTES, result, "stdout", overflow_event),
                daemon=True,
            ),
            threading.Thread(
                target=read_pipe,
                args=(err_read, MAX_STREAM_BYTES, result, "stderr", overflow_event),
                daemon=True,
            ),
        ]
        for thread in threads:
            thread.start()
            started_threads.append(thread)
        check_deadline(deadline, stage)
        if kernel32.ResumeThread(process.hThread) == 0xFFFFFFFF:
            raise win_error(f"ResumeThread({stage})")
        while True:
            wait = kernel32.WaitForSingleObject(
                process.hProcess,
                bounded_wait_milliseconds(deadline, 250, stage),
            )
            task_tree_bytes()
            if overflow_event.is_set():
                if result.get("stdout_reader_error") or result.get("stderr_reader_error"):
                    raise Blocked("resource", f"{stage} stream read failed")
                raise Blocked("resource", f"{stage} output exceeded 8 MiB")
            if wait == WAIT_OBJECT_0:
                check_deadline(deadline, stage)
                break
            if wait != WAIT_TIMEOUT:
                raise win_error(f"WaitForSingleObject({stage})")
        grace_deadline = min(
            deadline,
            global_deadline,
            time.monotonic() + ACTIVE_PROCESS_ZERO_GRACE_SECONDS,
        )
        while True:
            check_deadline(grace_deadline, stage)
            if overflow_event.is_set():
                if result.get("stdout_reader_error") or result.get("stderr_reader_error"):
                    raise Blocked("resource", f"{stage} stream read failed")
                raise Blocked("resource", f"{stage} output exceeded 8 MiB")
            readers_done = all(not thread.is_alive() for thread in threads)
            if readers_done and active_job_processes(worker_job) == 0:
                check_deadline(grace_deadline, stage)
                break
            time.sleep(
                min(JOB_POLL_SECONDS, max(0.0, grace_deadline - time.monotonic()))
            )
        if result.get("stdout_overflow") or result.get("stderr_overflow"):
            raise Blocked("resource", f"{stage} output exceeded 8 MiB")
        if result.get("stdout_reader_error") or result.get("stderr_reader_error"):
            raise Blocked("resource", f"{stage} stream read failed")
        if result.get("stdout_reader_cleanup_error") or result.get("stderr_reader_cleanup_error"):
            raise Blocked("resource", f"{stage} stream cleanup failed")
        check_deadline(grace_deadline, stage)
        exit_code = wintypes.DWORD()
        if not kernel32.GetExitCodeProcess(process.hProcess, ctypes.byref(exit_code)):
            raise win_error(f"GetExitCodeProcess({stage})")
        return int(exit_code.value), result.get("stdout", b""), result.get("stderr", b"")
    except BaseException as primary:
        try:
            if assigned:
                terminate_job_and_confirm_empty(worker_job, 128, stage, global_deadline)
            elif not assigned:
                wait = kernel32.WaitForSingleObject(process.hProcess, 0)
                if wait == WAIT_TIMEOUT:
                    if not kernel32.TerminateProcess(process.hProcess, 129):
                        raise win_error(f"TerminateProcess({stage})")
                    wait_ms = bounded_wait_milliseconds(global_deadline, 10000, stage)
                    if kernel32.WaitForSingleObject(process.hProcess, wait_ms) != WAIT_OBJECT_0:
                        raise Blocked("resource", f"{stage} process did not exit")
        except BaseException as cleanup:
            primary.add_note(f"process cleanup also failed: {type(cleanup).__name__}: {cleanup}")
        if started_threads:
            for thread in started_threads:
                thread.join(
                    timeout=max(
                        0.0,
                        global_deadline - time.monotonic(),
                    )
                )
            for thread in started_threads:
                if thread.is_alive():
                    primary.add_note(f"{stage} stream reader did not finish before deadline")
        try:
            setattr(primary, "captured_stdout", result.get("stdout", b""))
            setattr(primary, "captured_stderr", result.get("stderr", b""))
        except BaseException:
            pass
        raise
    finally:
        cleanup_errors: list[str] = []
        if started_threads:
            for thread in started_threads:
                thread.join(timeout=max(0.0, global_deadline - time.monotonic()))
            if any(thread.is_alive() for thread in started_threads):
                cleanup_errors.append("stream reader remained alive at cleanup deadline")
        unstarted_handles = (("stdout read", out_read), ("stderr read", err_read))[
            len(started_threads) :
        ]
        for label, handle in unstarted_handles:
            if not kernel32.CloseHandle(handle):
                cleanup_errors.append(
                    f"CloseHandle({label}) Windows error {ctypes.get_last_error()}"
                )
        for label, handle in (("process thread", process.hThread), ("process", process.hProcess)):
            if not kernel32.CloseHandle(handle):
                cleanup_errors.append(
                    f"CloseHandle({label}) Windows error {ctypes.get_last_error()}"
                )
        if cleanup_errors:
            active_exception = sys.exception()
            if active_exception is not None:
                for cleanup_error in cleanup_errors:
                    active_exception.add_note("worker cleanup also failed: " + cleanup_error)
            else:
                raise Blocked("resource", f"{stage} cleanup failed: {cleanup_errors[0]}")


def site_packages(venv: Path) -> Path:
    return venv / "Lib" / "site-packages"


def remove_venv_baseline_bytecode(venv: Path) -> dict[str, object]:
    resolved_venv = venv.resolve()
    if (
        not resolved_venv.is_relative_to(TASK_ROOT.resolve())
        or resolved_venv == TASK_ROOT.resolve()
        or not resolved_venv.is_dir()
        or resolved_venv.is_symlink()
        or resolved_venv.is_junction()
    ):
        raise Blocked("venv", "refusing bytecode cleanup outside regular task-owned venv")
    candidates = sorted(
        (
            path
            for path in resolved_venv.rglob("*")
            if path.name == "__pycache__" or path.suffix.casefold() == ".pyc"
        ),
        key=lambda path: (-len(path.parts), path.as_posix().casefold()),
    )
    if len(candidates) > MAX_INSTALLED_FILES:
        raise Blocked("venv", "baseline bytecode cleanup exceeds file cap")
    removed: list[str] = []
    for candidate in candidates:
        if not candidate.exists():
            continue
        resolved = candidate.resolve()
        if not resolved.is_relative_to(resolved_venv) or candidate.is_symlink():
            raise Blocked("venv", f"refusing link/escaped bytecode cleanup target: {candidate}")
        relative = candidate.relative_to(resolved_venv).as_posix()
        if candidate.is_dir():
            if candidate.is_junction():
                raise Blocked("venv", f"refusing bytecode junction: {candidate}")
            shutil.rmtree(candidate)
        elif candidate.is_file():
            candidate.unlink()
        else:
            raise Blocked("venv", f"unsupported bytecode cleanup target: {candidate}")
        removed.append(relative)
    residual = [
        path.relative_to(resolved_venv).as_posix()
        for path in resolved_venv.rglob("*")
        if path.name == "__pycache__" or path.suffix.casefold() == ".pyc"
    ]
    if residual:
        raise Blocked("venv", f"baseline bytecode cleanup left paths: {residual[:3]}")
    task_tree_bytes()
    return {"status": "REMOVED", "count": len(removed), "paths": sorted(removed)}


def distribution_inventory(site: Path) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for dist_info in sorted(site.glob("*.dist-info"), key=lambda path: path.name.casefold()):
        metadata_path = dist_info / "METADATA"
        if not metadata_path.is_file():
            continue
        metadata = email.parser.BytesParser().parsebytes(metadata_path.read_bytes())
        name = str(metadata.get("Name", "")).lower().replace("_", "-")
        if not name or name in result:
            raise Blocked("install", f"invalid/duplicate installed distribution {dist_info.name}")
        result[name] = {"version": str(metadata.get("Version", "")), "dist_info": dist_info.name}
    return result


def site_tree_snapshot(site: Path, global_deadline: float) -> dict[str, tuple[str, int]]:
    result: dict[str, tuple[str, int]] = {}
    folded: set[str] = set()
    for root, dirs, files in os.walk(site, followlinks=False):
        check_deadline(global_deadline, "installed tree inventory")
        root_path = Path(root)
        for name in dirs:
            entry = root_path / name
            if entry.is_symlink() or entry.is_junction():
                raise Blocked("install", f"installed tree contains directory link: {entry}")
        for name in files:
            entry = root_path / name
            if entry.is_symlink() or not entry.is_file():
                raise Blocked("install", f"installed tree contains nonregular file: {entry}")
            relative = entry.relative_to(site).as_posix()
            folded_name = relative.casefold()
            if folded_name in folded:
                raise Blocked("install", f"installed tree has colliding path: {relative}")
            digest, size = sha256_file(entry, cap=MAX_TASK_BYTES, deadline=global_deadline)
            result[relative] = (digest, size)
            folded.add(folded_name)
            if len(result) > MAX_INSTALLED_FILES * 2:
                raise Blocked("install", "complete site-packages tree exceeds bounded inventory cap")
    return result


def installed_member_path(site: Path, member: str, dist_info: str) -> Path:
    parts = PurePosixPath(member).parts
    marker = ".data"
    if parts and parts[0].endswith(marker) and len(parts) >= 3:
        scheme = parts[1]
        if scheme not in ("purelib", "platlib"):
            raise Blocked("install", f"unsupported wheel data scheme {scheme}")
        return site.joinpath(*parts[2:])
    return site.joinpath(*parts)


def parse_installed_record(record_path: Path) -> dict[str, tuple[str, str]]:
    rows = list(csv.reader(io.StringIO(record_path.read_text(encoding="utf-8"), newline="")))
    if len(rows) > MAX_INSTALLED_FILES:
        raise Blocked("install", "installed RECORD exceeds file cap")
    result: dict[str, tuple[str, str]] = {}
    folded: set[str] = set()
    for row in rows:
        if len(row) != 3:
            raise Blocked("install", "installed RECORD row arity mismatch")
        name, hash_value, size_value = row
        safe_zip_name(name)
        if name in result or name.casefold() in folded:
            raise Blocked("install", f"duplicate installed RECORD row {name}")
        result[name] = (hash_value, size_value)
        folded.add(name.casefold())
    return result


def verify_installed_files(
    site: Path,
    wheelhouse: Path,
    wheel_results: list[dict[str, object]],
    baseline_files: dict[str, tuple[str, int]],
    global_deadline: float,
) -> dict[str, object]:
    expected_names = {str(spec["name"]): str(spec["version"]) for spec in WHEELS}
    installed = distribution_inventory(site)
    for name, version in expected_names.items():
        if name not in installed or installed[name]["version"] != version:
            raise Blocked("install", f"missing/wrong installed distribution {name}=={version}")
    all_bytecode = [
        path.relative_to(site).as_posix()
        for path in site.rglob("*")
        if path.name == "__pycache__" or path.suffix.lower() == ".pyc"
    ]
    if all_bytecode:
        raise Blocked("install", f"bytecode paths present: {all_bytecode[:3]}")

    summaries: dict[str, object] = {}
    expected_new_paths: set[str] = set()
    for spec, wheel_result in zip(WHEELS, wheel_results, strict=True):
        check_deadline(global_deadline, "installed distribution verification")
        wheel_path = wheelhouse / str(spec["filename"])
        dist_info = str(wheel_result["dist_info"])
        record_path = site / dist_info / "RECORD"
        if not record_path.is_file():
            raise Blocked("install", f"missing installed RECORD for {spec['name']}")
        installed_record = parse_installed_record(record_path)
        archive_rows = {row[0]: (row[1], row[2]) for row in wheel_result["record"]["rows"]}
        archive_record_name = dist_info + "/RECORD"
        expected_paths = set(archive_rows)
        expected_paths.remove(archive_record_name)
        allowed = {
            dist_info + "/INSTALLER",
            dist_info + "/REQUESTED",
            dist_info + "/direct_url.json",
            dist_info + "/RECORD",
        }
        if set(installed_record) != expected_paths | allowed:
            missing = sorted((expected_paths | allowed) - set(installed_record))
            extra = sorted(set(installed_record) - (expected_paths | allowed))
            raise Blocked("install", f"installed file set mismatch missing={missing[:3]} extra={extra[:3]}")
        expected_new_paths.update(installed_record)
        if len(expected_new_paths) > MAX_INSTALLED_FILES:
            raise Blocked("install", "installed distribution aggregate exceeds file cap")
        with zipfile.ZipFile(wheel_path, "r") as archive:
            for member in expected_paths:
                target = installed_member_path(site, member, dist_info)
                if not target.is_file() or target.is_symlink():
                    raise Blocked("install", f"missing/nonregular installed payload {member}")
                digest, size = sha256_file(
                    target,
                    cap=MAX_TASK_BYTES,
                    deadline=global_deadline,
                )
                hash_value, size_value = archive_rows[member]
                _, encoded = decode_record_hash(hash_value)
                actual_encoded = base64.urlsafe_b64encode(bytes.fromhex(digest)).rstrip(b"=").decode("ascii")
                if actual_encoded != encoded or str(size) != size_value:
                    raise Blocked("install", f"installed payload differs from wheel: {member}")
        installer = site / dist_info / "INSTALLER"
        requested = site / dist_info / "REQUESTED"
        direct = site / dist_info / "direct_url.json"
        if installer.read_bytes() != b"pip\n" or requested.read_bytes() != b"":
            raise Blocked("install", f"invalid pip-added marker for {spec['name']}")
        direct_data = json.loads(direct.read_text(encoding="utf-8"))
        expected_url = wheel_path.resolve().as_uri()
        if set(direct_data) != {"archive_info", "url"} or direct_data.get("url") != expected_url:
            raise Blocked("install", f"invalid direct_url.json for {spec['name']}")
        archive_info = direct_data.get("archive_info")
        if not isinstance(archive_info, dict) or archive_info.get("hash") != "sha256=" + str(spec["sha256"]):
            raise Blocked("install", f"invalid direct_url hash for {spec['name']}")
        if set(archive_info) - {"hash", "hashes"}:
            raise Blocked("install", f"extra direct_url archive fields for {spec['name']}")
        if "hashes" in archive_info and archive_info["hashes"] != {"sha256": spec["sha256"]}:
            raise Blocked("install", f"invalid direct_url hashes for {spec['name']}")
        for member, (hash_value, size_value) in installed_record.items():
            target = site.joinpath(*PurePosixPath(member).parts)
            if member == dist_info + "/RECORD":
                if hash_value or size_value:
                    raise Blocked("install", "installed RECORD self row is not empty")
                continue
            if not target.is_file() or target.is_symlink():
                raise Blocked("install", f"installed RECORD target missing {member}")
            _, encoded = decode_record_hash(hash_value)
            digest, size = sha256_file(
                target,
                cap=MAX_TASK_BYTES,
                deadline=global_deadline,
            )
            actual_encoded = base64.urlsafe_b64encode(bytes.fromhex(digest)).rstrip(b"=").decode("ascii")
            if actual_encoded != encoded or str(size) != size_value:
                raise Blocked("install", f"installed RECORD hash/size mismatch {member}")
        summaries[str(spec["name"])] = {
            "version": spec["version"],
            "dist_info": dist_info,
            "record_rows": len(installed_record),
            "direct_url": expected_url,
        }
    post_files = site_tree_snapshot(site, global_deadline)
    baseline_paths = set(baseline_files)
    if not baseline_paths.issubset(post_files):
        raise Blocked("install", "pip removed a baseline site-packages file")
    changed_baseline = sorted(
        name for name, signature in baseline_files.items() if post_files[name] != signature
    )
    if changed_baseline:
        raise Blocked("install", f"pip changed baseline files: {changed_baseline[:3]}")
    actual_new_paths = set(post_files) - baseline_paths
    if actual_new_paths != expected_new_paths:
        missing = sorted(expected_new_paths - actual_new_paths)
        extra = sorted(actual_new_paths - expected_new_paths)
        raise Blocked(
            "install",
            f"unrecorded installed file delta missing={missing[:3]} extra={extra[:3]}",
        )
    return {
        "status": "VERIFIED",
        "distributions": summaries,
        "bytecode_paths": [],
        "baseline_file_count": len(baseline_files),
        "installed_delta_file_count": len(actual_new_paths),
    }


def stub_module_for(path: Path, site: Path) -> str:
    rel = path.relative_to(site)
    parts = list(rel.parts)
    first = parts[0]
    if first in ("OCP-stubs", "OCP"):
        parts[0] = "OCP"
    elif first.endswith("-stubs") and first[:-6] == "OCP":
        parts[0] = "OCP"
    if parts[-1] == "__init__.pyi":
        parts = parts[:-1]
    else:
        parts[-1] = Path(parts[-1]).stem
    return ".".join(parts)


def declaration_text(source: str, node: ast.AST) -> str:
    text = ast.get_source_segment(source, node) or ""
    data = text.encode("utf-8")
    if len(data) > MAX_DOC_BYTES:
        data = data[:MAX_DOC_BYTES]
        text = data.decode("utf-8", errors="ignore")
    return text


def collect_stub_declarations(site: Path) -> tuple[dict[str, list[dict[str, object]]], list[dict[str, object]]]:
    try:
        stub_distribution = importlib.metadata.distribution("cadquery-ocp-stubs")
    except importlib.metadata.PackageNotFoundError as exc:
        raise Blocked("inventory", "installed cadquery-ocp-stubs distribution is absent") from exc
    distribution_files = stub_distribution.files
    if distribution_files is None:
        raise Blocked("inventory", "stubs distribution exposes no installed file inventory")
    wanted_modules = {".".join(target.split(".")[:2]) for target in TARGETS}
    selected: dict[str, Path] = {}
    for entry in distribution_files:
        relative = PurePosixPath(str(entry).replace("\\", "/"))
        if relative.suffix != ".pyi":
            continue
        candidate = Path(stub_distribution.locate_file(entry)).resolve()
        if not candidate.is_relative_to(site.resolve()):
            raise Blocked("inventory", f"stub path escapes isolated site-packages: {entry}")
        module = stub_module_for(candidate, site.resolve())
        if module not in wanted_modules:
            continue
        key = candidate.as_posix().casefold()
        if key in selected:
            raise Blocked("inventory", f"duplicate selected stub path: {candidate}")
        selected[key] = candidate
    files = sorted(selected.values(), key=lambda path: path.as_posix().casefold())
    if len(files) > MAX_PYI_FILES:
        raise Blocked("inventory", f".pyi count exceeds {MAX_PYI_FILES}")
    if not files:
        raise Blocked("inventory", "no target-module stubs were selected")
    total = 0
    declarations: dict[str, list[dict[str, object]]] = {target: [] for target in TARGETS}
    provenance: list[dict[str, object]] = []
    declaration_count = 0
    for path in files:
        if not path.is_file() or path.is_symlink():
            raise Blocked("inventory", f"stub is not a regular file: {path}")
        size = path.stat().st_size
        if size > MAX_PYI_BYTES:
            raise Blocked("inventory", f"{path.name} exceeds .pyi file cap")
        total += size
        if total > MAX_PYI_TOTAL:
            raise Blocked("inventory", ".pyi aggregate exceeds cap")
        file_hash, hashed_size = sha256_file(path, cap=MAX_PYI_BYTES)
        if hashed_size != size:
            raise Blocked("inventory", f"stub size changed during streamed hash: {path}")
        digest = hashlib.sha256()
        chunks = bytearray()
        with path.open("rb") as stream:
            while True:
                chunk = stream.read(HASH_CHUNK)
                if not chunk:
                    break
                if len(chunks) + len(chunk) > size:
                    raise Blocked("inventory", f"stub grew during bounded read: {path}")
                chunks.extend(chunk)
                digest.update(chunk)
        data = bytes(chunks)
        if len(data) != size or digest.hexdigest() != file_hash:
            raise Blocked("inventory", f"stub changed between streamed hash/read: {path}")
        try:
            source = data.decode("utf-8")
            tree = ast.parse(source, filename=str(path), type_comments=True)
        except Exception as exc:
            raise Blocked("inventory", f"stub AST parse failed for {path}: {exc}") from exc
        module = stub_module_for(path, site)
        rel = path.relative_to(site).as_posix()
        provenance.append({"path": rel, "bytes": len(data), "sha256": file_hash})

        def visit(body: list[ast.stmt], prefix: str) -> None:
            nonlocal declaration_count
            for node in body:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    qualified = prefix + "." + node.name
                    if qualified in declarations:
                        declaration_count += 1
                        if declaration_count > MAX_DECLARATIONS:
                            raise Blocked("inventory", "target declaration count exceeds cap")
                        item: dict[str, object] = {
                            "path": rel,
                            "file_sha256": file_hash,
                            "line_start": node.lineno,
                            "line_end": getattr(node, "end_lineno", node.lineno),
                            "kind": type(node).__name__,
                            "source": declaration_text(source, node),
                        }
                        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            item["positional_parameters"] = [arg.arg for arg in node.args.posonlyargs + node.args.args]
                            item["keyword_only_parameters"] = [arg.arg for arg in node.args.kwonlyargs]
                            item["vararg"] = node.args.vararg.arg if node.args.vararg else None
                            item["kwarg"] = node.args.kwarg.arg if node.args.kwarg else None
                            item["defaults"] = len(node.args.defaults)
                            item["keyword_defaults"] = sum(
                                default is not None for default in node.args.kw_defaults
                            )
                            item["return_annotation"] = ast.unparse(node.returns) if node.returns else None
                            item["decorators"] = [ast.unparse(dec) for dec in node.decorator_list]
                        declarations[qualified].append(item)
                    if isinstance(node, ast.ClassDef):
                        visit(node.body, qualified)
                elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                    assigned_names: list[str] = []
                    if isinstance(node, ast.Assign):
                        assigned_names = [
                            target.id for target in node.targets if isinstance(target, ast.Name)
                        ]
                    elif isinstance(node.target, ast.Name):
                        assigned_names = [node.target.id]
                    for name in assigned_names:
                        qualified = prefix + "." + name
                        if qualified not in declarations:
                            continue
                        declaration_count += 1
                        if declaration_count > MAX_DECLARATIONS:
                            raise Blocked("inventory", "target declaration count exceeds cap")
                        declarations[qualified].append(
                            {
                                "path": rel,
                                "file_sha256": file_hash,
                                "line_start": node.lineno,
                                "line_end": getattr(node, "end_lineno", node.lineno),
                                "kind": type(node).__name__,
                                "source": declaration_text(source, node),
                            }
                        )

        visit(tree.body, module)
    return declarations, provenance


def declaration_runtime_conclusion(
    declaration: dict[str, object],
    runtime: object,
    signature: inspect.Signature | None,
) -> tuple[str, str]:
    kind = declaration.get("kind")
    if kind == "ClassDef":
        return (
            ("AGREE", "stub and runtime are classes")
            if inspect.isclass(runtime)
            else ("CONFLICT", "stub declares a class but runtime is not a class")
        )
    if kind in ("Assign", "AnnAssign"):
        return (
            ("AGREE", "stub and runtime expose a non-callable value")
            if not callable(runtime)
            else ("CONFLICT", "stub declares a value but runtime is callable")
        )
    if kind not in ("FunctionDef", "AsyncFunctionDef"):
        return "AMBIGUOUS", f"unsupported stub declaration kind {kind!r}"
    if not callable(runtime):
        return "CONFLICT", "stub declares a callable but runtime is not callable"
    if signature is None:
        return "AMBIGUOUS", "runtime signature is unavailable"
    parameters = list(signature.parameters.values())
    runtime_positional = [
        parameter.name
        for parameter in parameters
        if parameter.kind
        in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD)
    ]
    runtime_keyword_only = [
        parameter.name
        for parameter in parameters
        if parameter.kind is inspect.Parameter.KEYWORD_ONLY
    ]
    runtime_vararg = next(
        (parameter.name for parameter in parameters if parameter.kind is inspect.Parameter.VAR_POSITIONAL),
        None,
    )
    runtime_kwarg = next(
        (parameter.name for parameter in parameters if parameter.kind is inspect.Parameter.VAR_KEYWORD),
        None,
    )
    runtime_defaults = sum(
        parameter.default is not inspect.Parameter.empty
        for parameter in parameters
        if parameter.kind
        in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD)
    )
    runtime_keyword_defaults = sum(
        parameter.default is not inspect.Parameter.empty
        for parameter in parameters
        if parameter.kind is inspect.Parameter.KEYWORD_ONLY
    )
    observed = {
        "positional_parameters": runtime_positional,
        "keyword_only_parameters": runtime_keyword_only,
        "vararg": runtime_vararg,
        "kwarg": runtime_kwarg,
        "defaults": runtime_defaults,
        "keyword_defaults": runtime_keyword_defaults,
    }
    declared = {key: declaration.get(key) for key in observed}
    if observed == declared:
        return "AGREE", "stub and runtime call shapes match exactly"
    return "CONFLICT", f"stub/runtime call-shape mismatch declared={declared} observed={observed}"


def bounded_text(value: object, aggregate: list[int]) -> dict[str, object]:
    if value is None:
        text = ""
    elif isinstance(value, str):
        text = value
    else:
        text = repr(value)
    data = text.encode("utf-8", errors="replace")
    original = len(data)
    digest = sha256_bytes(data)
    truncated = original > MAX_DOC_BYTES
    if truncated:
        data = data[:MAX_DOC_BYTES]
        text = data.decode("utf-8", errors="ignore")
        data = text.encode("utf-8")
    aggregate[0] += len(data)
    if aggregate[0] > MAX_DOC_TOTAL:
        raise Blocked("inventory", "aggregate captured docs/signatures exceeds cap")
    return {"text": text, "original_bytes": original, "sha256": digest, "truncated": truncated}


def resolve_target(target: str):
    parts = target.split(".")
    module = importlib.import_module(".".join(parts[:2]))
    current = module
    for part in parts[2:]:
        current = getattr(current, part)
    return current


def inventory_main() -> int:
    if len(TARGETS) > MAX_DECLARATIONS:
        raise Blocked("inventory", "target count exceeds declaration cap")
    site = Path(sys.prefix) / "Lib" / "site-packages"
    declarations, stub_files = collect_stub_declarations(site)
    stub_declaration_bytes = sum(
        len(str(item.get("source", "")).encode("utf-8"))
        for items in declarations.values()
        for item in items
    )
    if stub_declaration_bytes > MAX_DOC_TOTAL:
        raise Blocked("inventory", "captured stub declarations exceed aggregate text cap")
    version_decls = declarations[VERSION_TARGET]
    if len(version_decls) != 1:
        raise Blocked("version", f"version target has {len(version_decls)} stub declarations")
    version_decl = version_decls[0]
    if (
        version_decl.get("positional_parameters") != []
        or version_decl.get("keyword_only_parameters") != []
        or version_decl.get("vararg") is not None
        or version_decl.get("kwarg") is not None
        or version_decl.get("return_annotation") != "str"
    ):
        raise Blocked("version", "version stub is not unambiguously () -> str")

    aggregate = [stub_declaration_bytes]
    targets: list[dict[str, object]] = []
    for target in TARGETS:
        item: dict[str, object] = {"target": target, "segments_exist": [], "declarations": declarations[target]}
        parts = target.split(".")
        runtime_object: object | None = None
        runtime_signature: inspect.Signature | None = None
        try:
            module = importlib.import_module(".".join(parts[:2]))
            current = module
            item["segments_exist"].append(".".join(parts[:2]))
            for part in parts[2:]:
                current = getattr(current, part)
                item["segments_exist"].append(part)
            runtime_object = current
            item["runtime_exists"] = True
            item["runtime_type"] = type(current).__module__ + "." + type(current).__qualname__
            item["callable"] = callable(current)
            item["is_class"] = inspect.isclass(current)
            try:
                runtime_signature = inspect.signature(current)
                item["signature"] = {
                    "value": bounded_text(str(runtime_signature), aggregate),
                    "error": None,
                }
            except Exception as exc:
                error_text = type(exc).__module__ + "." + type(exc).__qualname__ + ": " + str(exc)
                item["signature"] = {
                    "value": None,
                    "error": bounded_text(error_text, aggregate),
                }
            item["text_signature"] = bounded_text(getattr(current, "__text_signature__", None), aggregate)
            item["doc"] = bounded_text(getattr(current, "__doc__", None), aggregate)
        except Exception as exc:
            item["runtime_exists"] = False
            item["runtime_error"] = type(exc).__module__ + "." + type(exc).__qualname__ + ": " + str(exc)
        if not item.get("runtime_exists") or not item["declarations"]:
            item["conclusion"] = "MISSING"
            item["conclusion_reason"] = "runtime object or stub declaration is missing"
        elif len(item["declarations"]) != 1:
            item["conclusion"] = "AMBIGUOUS"
            item["conclusion_reason"] = "multiple stub declarations/overloads require a later exact call probe"
        else:
            conclusion, reason = declaration_runtime_conclusion(
                item["declarations"][0],
                runtime_object,
                runtime_signature,
            )
            item["conclusion"] = conclusion
            item["conclusion_reason"] = reason
        targets.append(item)

    version_function = resolve_target(VERSION_TARGET)
    version_value = version_function()  # The sole permitted native call.
    if not isinstance(version_value, str):
        raise Blocked("version", f"version result is {type(version_value).__name__}, not str")
    match = re.match(r"^\s*(\d+)\.(\d+)\.(\d+)", version_value)
    if match is None or tuple(match.groups()) != ("7", "9", "3"):
        raise Blocked("version", f"runtime OCCT version is not 7.9.3: {version_value!r}")
    forbidden = sorted(
        name for name in sys.modules if name.split(".", 1)[0].lower() in {
            "cadquery", "vtk", "anygeometry", "anyfem"
        }
    )
    if forbidden:
        raise Blocked("isolation", f"forbidden imported modules: {forbidden[:10]}")
    ocp = importlib.import_module("OCP")
    ocp_origin = str(Path(ocp.__file__).resolve())
    if not Path(ocp_origin).is_relative_to(site.resolve()):
        raise Blocked("isolation", f"OCP origin outside isolated site-packages: {ocp_origin}")
    repo_paths = [value for value in sys.path if value and "\\Github\\" in str(Path(value).resolve())]
    if repo_paths:
        raise Blocked("isolation", f"repository source paths present: {repo_paths}")
    output = {
        "schema": 1,
        "status": "PASS",
        "runtime_occt_version": version_value,
        "version_target": VERSION_TARGET,
        "version_calls": 1,
        "distribution_version_is_not_runtime_version": True,
        "ocp_origin": ocp_origin,
        "forbidden_modules": [],
        "repo_source_paths": [],
        "candidate_setting_keys_not_queried": list(CANDIDATE_SETTING_KEYS),
        "stub_files": stub_files,
        "stub_file_count": len(stub_files),
        "stub_aggregate_bytes": sum(item["bytes"] for item in stub_files),
        "stub_declaration_bytes": stub_declaration_bytes,
        "captured_doc_signature_bytes": aggregate[0],
        "targets": targets,
    }
    data = canonical_json_bytes(output)
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()
    return 0


def host_facts() -> dict[str, object]:
    return {
        "executable": str(Path(sys.executable).resolve()),
        "implementation": platform.python_implementation(),
        "python_version": platform.python_version(),
        "python_full": sys.version,
        "bits": struct.calcsize("P") * 8,
        "platform": platform.platform(),
        "machine": platform.machine(),
    }


def validate_predecessor_receipt() -> None:
    if (
        not RETIRED_RECEIPT.is_dir()
        or RETIRED_RECEIPT.is_symlink()
        or RETIRED_RECEIPT.is_junction()
        or RETIRED_FINAL_ROOT.exists()
    ):
        raise Blocked("preflight", "immutable predecessor receipt/final state drifted")
    entries = sorted(RETIRED_RECEIPT.iterdir(), key=lambda path: path.name)
    if [path.name for path in entries] != sorted(EVIDENCE_NAMES):
        raise Blocked("preflight", "immutable predecessor receipt inventory drifted")
    total = 0
    for path in entries:
        if not path.is_file() or path.is_symlink():
            raise Blocked("preflight", f"predecessor receipt contains nonregular {path.name}")
        total += path.stat().st_size
    if total != RETIRED_RECEIPT_BYTES:
        raise Blocked("preflight", "immutable predecessor receipt byte count drifted")
    sums_hash, _ = sha256_file(
        RETIRED_RECEIPT / "SHA256SUMS.txt",
        cap=MAX_EVIDENCE_BYTES,
    )
    outcome_hash, _ = sha256_file(
        RETIRED_RECEIPT / "OUTCOME.json",
        cap=MAX_JSON_BYTES,
    )
    if (
        sums_hash != RETIRED_RECEIPT_SUMS_SHA256
        or outcome_hash != RETIRED_RECEIPT_OUTCOME_SHA256
    ):
        raise Blocked("preflight", "immutable predecessor receipt hashes drifted")
    try:
        sums_lines = (RETIRED_RECEIPT / "SHA256SUMS.txt").read_text(
            encoding="ascii"
        ).splitlines()
    except Exception as exc:
        raise Blocked("preflight", "immutable predecessor sums are unreadable") from exc
    if len(sums_lines) != len(HASHED_EVIDENCE_NAMES):
        raise Blocked("preflight", "immutable predecessor sums line count drifted")
    parsed: list[tuple[str, int, str]] = []
    for line in sums_lines:
        match = re.fullmatch(r"([0-9a-f]{64})  ([0-9]+)  ([A-Za-z0-9_.-]+)", line)
        if match is None:
            raise Blocked("preflight", "immutable predecessor sums syntax drifted")
        parsed.append((match.group(1), int(match.group(2)), match.group(3)))
    if [item[2] for item in parsed] != list(HASHED_EVIDENCE_NAMES):
        raise Blocked("preflight", "immutable predecessor sums inventory drifted")
    for expected_hash, expected_size, name in parsed:
        actual_hash, actual_size = sha256_file(
            RETIRED_RECEIPT / name,
            cap=MAX_EVIDENCE_BYTES,
        )
        if actual_hash != expected_hash or actual_size != expected_size:
            raise Blocked("preflight", f"immutable predecessor payload drifted: {name}")


def validate_v2_predecessor() -> None:
    if (
        not V2_FINAL_ROOT.is_dir()
        or V2_FINAL_ROOT.is_symlink()
        or V2_FINAL_ROOT.is_junction()
        or any(path.exists() for path in (V2_PENDING_ROOT, V2_SENTRY_TEMP, V2_SENTRY))
    ):
        raise Blocked("preflight", "immutable V2 evidence state drifted")
    entries = sorted(V2_FINAL_ROOT.iterdir(), key=lambda path: path.name)
    if [path.name for path in entries] != sorted(EVIDENCE_NAMES):
        raise Blocked("preflight", "immutable V2 evidence inventory drifted")
    total = 0
    for path in entries:
        if not path.is_file() or path.is_symlink():
            raise Blocked("preflight", f"V2 evidence contains nonregular {path.name}")
        total += path.stat().st_size
    if total != V2_FINAL_BYTES:
        raise Blocked("preflight", "immutable V2 evidence byte count drifted")
    sums_hash, _ = sha256_file(V2_FINAL_ROOT / "SHA256SUMS.txt", cap=MAX_EVIDENCE_BYTES)
    outcome_hash, _ = sha256_file(V2_FINAL_ROOT / "OUTCOME.json", cap=MAX_JSON_BYTES)
    if sums_hash != V2_SUMS_SHA256 or outcome_hash != V2_OUTCOME_SHA256:
        raise Blocked("preflight", "immutable V2 evidence hashes drifted")
    try:
        sums_lines = (V2_FINAL_ROOT / "SHA256SUMS.txt").read_text(
            encoding="ascii"
        ).splitlines()
    except Exception as exc:
        raise Blocked("preflight", "immutable V2 sums are unreadable") from exc
    if len(sums_lines) != len(HASHED_EVIDENCE_NAMES):
        raise Blocked("preflight", "immutable V2 sums line count drifted")
    for expected_name, line in zip(HASHED_EVIDENCE_NAMES, sums_lines, strict=True):
        match = re.fullmatch(r"([0-9a-f]{64})  ([0-9]+)  ([A-Za-z0-9_.-]+)", line)
        if match is None or match.group(3) != expected_name:
            raise Blocked("preflight", "immutable V2 sums inventory drifted")
        actual_hash, actual_size = sha256_file(
            V2_FINAL_ROOT / expected_name,
            cap=MAX_EVIDENCE_BYTES,
        )
        if actual_hash != match.group(1) or actual_size != int(match.group(2)):
            raise Blocked("preflight", f"immutable V2 payload drifted: {expected_name}")

    if not V2_TASK_ROOT.is_dir() or V2_TASK_ROOT.is_symlink() or V2_TASK_ROOT.is_junction():
        raise Blocked("preflight", "V2 task root is missing/link-like")
    task_entries = sorted(V2_TASK_ROOT.iterdir(), key=lambda path: path.name)
    if [path.name for path in task_entries] != ["probe.py", "tmp", "wheelhouse"]:
        raise Blocked("preflight", "V2 task inventory drifted")
    v2_probe = V2_TASK_ROOT / "probe.py"
    probe_hash, probe_size = sha256_file(v2_probe, cap=MAX_JSON_BYTES)
    if probe_hash != V2_PROBE_SHA256 or probe_size != 139062 or v2_probe.is_symlink():
        raise Blocked("preflight", "V2 probe drifted")
    v2_tmp = V2_TASK_ROOT / "tmp"
    if (
        not v2_tmp.is_dir()
        or v2_tmp.is_symlink()
        or v2_tmp.is_junction()
        or list(v2_tmp.iterdir())
    ):
        raise Blocked("preflight", "V2 tmp state drifted")
    if (
        not V2_WHEELHOUSE.is_dir()
        or V2_WHEELHOUSE.is_symlink()
        or V2_WHEELHOUSE.is_junction()
    ):
        raise Blocked("preflight", "V2 wheelhouse is missing/link-like")
    wheel_entries = sorted(V2_WHEELHOUSE.iterdir(), key=lambda path: path.name)
    if [path.name for path in wheel_entries] != sorted(str(spec["filename"]) for spec in WHEELS):
        raise Blocked("preflight", "V2 wheelhouse inventory drifted")
    for spec in WHEELS:
        source = V2_WHEELHOUSE / str(spec["filename"])
        if not source.is_file() or source.is_symlink():
            raise Blocked("preflight", f"V2 wheel is nonregular: {source.name}")
        digest, size = sha256_file(source, cap=int(spec["bytes"]))
        if digest != spec["sha256"] or size != spec["bytes"]:
            raise Blocked("preflight", f"V2 wheel drifted: {source.name}")


def reuse_wheel(
    spec: dict[str, object],
    destination: Path,
    reuse_deadline: float,
) -> dict[str, object]:
    source = V2_WHEELHOUSE / str(spec["filename"])
    part = destination.with_name(destination.name + ".part")
    if destination.exists() or part.exists():
        raise Blocked("wheel-reuse", f"V3 wheel target already exists: {destination.name}")
    source_hash, source_size = sha256_file(
        source,
        cap=int(spec["bytes"]),
        deadline=reuse_deadline,
    )
    if source_hash != spec["sha256"] or source_size != spec["bytes"]:
        raise Blocked("wheel-reuse", f"V2 source wheel drifted: {source.name}")
    digest = hashlib.sha256()
    copied = 0
    try:
        with source.open("rb") as input_stream, part.open("xb") as output_stream:
            while True:
                check_deadline(reuse_deadline, "wheel reuse")
                remaining = int(spec["bytes"]) - copied
                chunk = input_stream.read(min(HASH_CHUNK, remaining + 1))
                if not chunk:
                    break
                if len(chunk) > remaining:
                    raise Blocked("wheel-reuse", "source wheel exceeds frozen byte count")
                output_stream.write(chunk)
                digest.update(chunk)
                copied += len(chunk)
                task_tree_bytes()
            output_stream.flush()
            os.fsync(output_stream.fileno())
        if copied != spec["bytes"] or digest.hexdigest() != spec["sha256"]:
            raise Blocked("wheel-reuse", f"copied wheel mismatch: {source.name}")
        if not kernel32.MoveFileExW(str(part), str(destination), MOVEFILE_WRITE_THROUGH):
            raise win_error("MoveFileExW(reuse wheel)")
        source_hash_after, source_size_after = sha256_file(
            source,
            cap=int(spec["bytes"]),
            deadline=reuse_deadline,
        )
        destination_hash, destination_size = sha256_file(
            destination,
            cap=int(spec["bytes"]),
            deadline=reuse_deadline,
        )
        if (
            (source_hash_after, source_size_after) != (source_hash, source_size)
            or destination_hash != spec["sha256"]
            or destination_size != spec["bytes"]
        ):
            raise Blocked("wheel-reuse", f"wheel changed during local reuse: {source.name}")
    except BaseException:
        if part.exists() and part.is_file() and not part.is_symlink():
            part.unlink()
        raise
    return {
        "stage": "local-reuse:" + str(spec["key"]),
        "method": "LOCAL_REUSE",
        "status": "VERIFIED",
        "source_path": str(source.resolve()),
        "destination_path": str(destination.resolve()),
        "bytes": destination_size,
        "sha256": destination_hash,
    }


def preflight_controller(probe: Path) -> None:
    if Path(sys.executable).resolve() != HOST_PYTHON.resolve():
        raise Blocked("preflight", f"wrong controller interpreter: {sys.executable}")
    facts = host_facts()
    if (
        facts["implementation"] != "CPython"
        or facts["python_version"] != "3.13.9"
        or sys.version_info.releaselevel != "final"
    ):
        raise Blocked("preflight", "host Python is not CPython 3.13.9")
    if (
        facts["bits"] != 64
        or facts["machine"].upper() != "AMD64"
        or os.name != "nt"
        or platform.release() != "11"
    ):
        raise Blocked("preflight", "host is not Windows 11 AMD64 64-bit")
    if probe.resolve() != (TASK_ROOT / "probe.py").resolve():
        raise Blocked("preflight", "probe path is not the registered task path")
    if not TASK_ROOT.is_dir() or TASK_ROOT.is_symlink() or TASK_ROOT.is_junction():
        raise Blocked("preflight", "registered task root is missing/link-like")
    entries = sorted(TASK_ROOT.iterdir(), key=lambda path: path.name)
    if [path.name for path in entries] != ["probe.py"]:
        raise Blocked("preflight", "task root does not contain only the frozen probe")
    if not probe.is_file() or probe.is_symlink():
        raise Blocked("preflight", "probe is not a regular non-link file")
    evidence_parent = FINAL_ROOT.parent
    if evidence_parent != PENDING_ROOT.parent:
        raise Blocked("preflight", "pending/final evidence parents differ")
    if (
        not evidence_parent.is_dir()
        or evidence_parent.is_symlink()
        or evidence_parent.is_junction()
    ):
        raise Blocked("preflight", "evidence parent is missing/link-like")
    if any(path.exists() for path in (FINAL_ROOT, PENDING_ROOT, SENTRY_TEMP, SENTRY)):
        raise Blocked("preflight", "V3 final, pending, or sentry path already exists")
    validate_predecessor_receipt()
    validate_v2_predecessor()
    if importlib.util.find_spec("OCP") is not None:
        raise Blocked("preflight", "host OCP import spec is present")
    present_distributions = []
    for name in ("cadquery-ocp-novtk", "cadquery-ocp-proxy", "cadquery-ocp-stubs"):
        try:
            importlib.metadata.distribution(name)
        except importlib.metadata.PackageNotFoundError:
            continue
        present_distributions.append(name)
    if present_distributions:
        raise Blocked("preflight", f"host distributions present: {present_distributions}")
    if not FOUNDATION_ROOT.is_dir() or FOUNDATION_ROOT.is_symlink() or FOUNDATION_ROOT.is_junction():
        raise Blocked("preflight", "foundation checkout is missing/link-like")
    if shutil.disk_usage(TASK_ROOT.anchor).free < 1024 * MIB:
        raise Blocked("preflight", "less than 1 GiB free disk")


def exercise_evidence_staging() -> None:
    assert kernel32 is not None
    parent = FINAL_ROOT.parent
    if (
        parent != PENDING_ROOT.parent
        or parent != SENTRY_TEMP.parent
        or parent != SENTRY.parent
        or not parent.is_dir()
        or parent.is_symlink()
        or parent.is_junction()
    ):
        raise Blocked("evidence-staging", "V3 evidence parent is missing/link-like")
    if any(path.exists() for path in (FINAL_ROOT, PENDING_ROOT, SENTRY_TEMP, SENTRY)):
        raise Blocked("evidence-staging", "V3 evidence or sentry path already exists")
    try:
        with SENTRY_TEMP.open("xb") as stream:
            stream.write(SENTRY_PAYLOAD)
            stream.flush()
            os.fsync(stream.fileno())
        if not kernel32.MoveFileExW(str(SENTRY_TEMP), str(SENTRY), MOVEFILE_WRITE_THROUGH):
            raise win_error("MoveFileExW(staging sentry)")
        if SENTRY_TEMP.exists() or not SENTRY.is_file() or SENTRY.is_symlink():
            raise Blocked("evidence-staging", "staging sentry rename did not linearize")
        digest, size = sha256_file(SENTRY, cap=len(SENTRY_PAYLOAD))
        if size != len(SENTRY_PAYLOAD) or digest != sha256_bytes(SENTRY_PAYLOAD):
            raise Blocked("evidence-staging", "staging sentry content changed")
        SENTRY.unlink()
        if SENTRY_TEMP.exists() or SENTRY.exists():
            raise Blocked("evidence-staging", "staging sentry cleanup did not linearize")
    except BaseException as primary:
        for path in (SENTRY_TEMP, SENTRY):
            try:
                if path.exists() and path.is_file() and not path.is_symlink():
                    path.unlink()
            except BaseException as cleanup:
                primary.add_note(
                    f"sentry cleanup also failed for {path.name}: "
                    f"{type(cleanup).__name__}: {cleanup}"
                )
        raise


def foundation_preflight(
    worker_job,
    environment: dict[str, str],
    global_deadline: float,
    commands: list[dict[str, object]],
) -> None:
    git = shutil.which("git")
    if not git:
        raise Blocked("preflight", "git executable is unavailable")
    identity_argv = [
        git,
        "-C",
        str(FOUNDATION_ROOT),
        "rev-parse",
        "HEAD",
        "HEAD^{tree}",
    ]
    exit_code, stdout, stderr = run_worker(
        worker_job,
        identity_argv,
        cwd=TASK_ROOT,
        environment=environment,
        stage="foundation-identity",
        seconds=30.0,
        global_deadline=global_deadline,
    )
    commands.append({"stage": "foundation-identity", "argv": identity_argv, "exit": exit_code})
    lines = stdout.decode("ascii", "strict").splitlines() if exit_code == 0 and not stderr else []
    if lines != [FOUNDATION_COMMIT, FOUNDATION_TREE]:
        raise Blocked(
            "preflight",
            f"foundation identity drift exit={exit_code} stdout={lines} stderr={stderr[-500:]!r}",
        )
    status_argv = [
        git,
        "-C",
        str(FOUNDATION_ROOT),
        "status",
        "--porcelain=v1",
        "--untracked-files=all",
    ]
    exit_code, stdout, stderr = run_worker(
        worker_job,
        status_argv,
        cwd=TASK_ROOT,
        environment=environment,
        stage="foundation-status",
        seconds=30.0,
        global_deadline=global_deadline,
    )
    commands.append({"stage": "foundation-status", "argv": status_argv, "exit": exit_code})
    if exit_code != 0 or stdout or stderr:
        raise Blocked(
            "preflight",
            f"foundation checkout is not clean exit={exit_code} stdout={stdout[-500:]!r} stderr={stderr[-500:]!r}",
        )


def write_atomic(path: Path, data: bytes) -> None:
    temp = path.with_name("." + path.name + ".tmp")
    if path.exists() or temp.exists():
        raise Blocked("publication", f"evidence target/temp already exists: {path.name}")
    with temp.open("xb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)


def placeholder_api(status: str) -> dict[str, object]:
    return {
        "schema": 1,
        "status": status,
        "runtime_occt_version": None,
        "version_target": VERSION_TARGET,
        "version_calls": 0,
        "targets": [],
        "stub_files": [],
    }


def stage_evidence(
    *,
    probe_bytes: bytes,
    wheel_document: dict[str, object],
    api_document: dict[str, object],
    outcome: dict[str, object],
    stdout: bytes,
    stderr: bytes,
) -> None:
    evidence_parent = FINAL_ROOT.parent
    if (
        evidence_parent != PENDING_ROOT.parent
        or not evidence_parent.is_dir()
        or evidence_parent.is_symlink()
        or evidence_parent.is_junction()
    ):
        raise Blocked("publication", "evidence parent is missing/link-like")
    if PENDING_ROOT.exists() or FINAL_ROOT.exists():
        raise Blocked("publication", "pending/final evidence root exists")
    PENDING_ROOT.mkdir(parents=False, exist_ok=False)
    payloads = {
        "PROBE.py": probe_bytes,
        "WHEELS.json": canonical_json_bytes(wheel_document),
        "API_INVENTORY.json": canonical_json_bytes(api_document),
        "OUTCOME.json": canonical_json_bytes(outcome),
        "STDOUT.txt": stdout,
        "STDERR.txt": stderr,
    }
    if len(stdout) > MAX_STREAM_BYTES or len(stderr) > MAX_STREAM_BYTES:
        raise Blocked("publication", "stream evidence exceeds cap")
    if sum(len(data) for data in payloads.values()) > MAX_EVIDENCE_BYTES:
        raise Blocked("publication", "evidence payload exceeds 32 MiB")
    for name in EVIDENCE_NAMES[:-1]:
        write_atomic(PENDING_ROOT / name, payloads[name])
    lines = []
    for name in HASHED_EVIDENCE_NAMES:
        data = payloads[name]
        lines.append(f"{sha256_bytes(data)}  {len(data)}  {name}\n")
    sums = "".join(lines).encode("ascii")
    write_atomic(PENDING_ROOT / "SHA256SUMS.txt", sums)


def require_bounded_int(value: object, maximum: int, label: str) -> int:
    if type(value) is not int or value < 0 or value > maximum:
        raise Blocked("validation", f"invalid bounded integer for {label}: {value!r}")
    return value


def require_sha256(value: object, label: str) -> str:
    if not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{64}", value) is None:
        raise Blocked("validation", f"invalid sha256 for {label}")
    return value


def validate_bounded_text(value: object, label: str) -> int:
    if not isinstance(value, dict) or set(value) != {
        "text",
        "original_bytes",
        "sha256",
        "truncated",
    }:
        raise Blocked("validation", f"invalid bounded-text projection for {label}")
    text = value.get("text")
    truncated = value.get("truncated")
    if not isinstance(text, str) or type(truncated) is not bool:
        raise Blocked("validation", f"invalid bounded-text value for {label}")
    encoded = text.encode("utf-8")
    if len(encoded) > MAX_DOC_BYTES:
        raise Blocked("validation", f"bounded text exceeds per-field cap for {label}")
    original_bytes = require_bounded_int(
        value.get("original_bytes"),
        MAX_JSON_BYTES,
        label + " original bytes",
    )
    digest = require_sha256(value.get("sha256"), label)
    if truncated:
        if original_bytes <= len(encoded):
            raise Blocked("validation", f"invalid truncated bounded text for {label}")
    elif original_bytes != len(encoded) or sha256_bytes(encoded) != digest:
        raise Blocked("validation", f"untruncated bounded text/hash mismatch for {label}")
    return len(encoded)


def validate_wheel_evidence(
    wheels: dict[str, object],
    first_failure: object,
) -> None:
    artifacts = wheels["artifacts"]
    local_sources = wheels["local_sources"]
    if len(artifacts) > len(WHEELS) or len(local_sources) > len(WHEELS):
        raise Blocked("validation", "wheel artifact/local-source count exceeds three")
    blocked_reuse_seen = False
    for index, source_record in enumerate(local_sources):
        if not isinstance(source_record, dict):
            raise Blocked("validation", "local-source evidence is not an object")
        spec = WHEELS[index]
        expected_source = str((V2_WHEELHOUSE / str(spec["filename"])).resolve())
        expected_destination = str((TASK_ROOT / "wheelhouse" / str(spec["filename"])).resolve())
        status = source_record.get("status")
        if (
            source_record.get("stage") != "local-reuse:" + str(spec["key"])
            or source_record.get("method") != "LOCAL_REUSE"
            or status not in {"BLOCKED", "VERIFIED"}
            or source_record.get("source_path") != expected_source
            or source_record.get("destination_path") != expected_destination
        ):
            raise Blocked("validation", f"local-source evidence {index} drifted")
        if status == "VERIFIED":
            if blocked_reuse_seen:
                raise Blocked("validation", "verified reuse follows blocked reuse")
            if (
                source_record.get("sha256") != spec["sha256"]
                or source_record.get("bytes") != spec["bytes"]
                or source_record.get("failure") is not None
            ):
                raise Blocked("validation", f"verified local-source evidence {index} drifted")
        else:
            blocked_reuse_seen = True
            if index != len(local_sources) - 1:
                raise Blocked("validation", "blocked reuse is not terminal")
            if (
                source_record.get("sha256") is not None
                or source_record.get("bytes") is not None
                or not isinstance(first_failure, dict)
                or source_record.get("failure") != first_failure
            ):
                raise Blocked("validation", f"blocked local-source evidence {index} is inconsistent")
    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            raise Blocked("validation", "wheel artifact is not an object")
        spec = WHEELS[index]
        if artifact.get("status") != "VERIFIED":
            raise Blocked("validation", f"wheel artifact {index} is not VERIFIED")
        for key in ("filename", "original_url", "source_path", "sha256", "tag"):
            if key == "original_url":
                expected = spec["url"]
            elif key == "source_path":
                expected = str((V2_WHEELHOUSE / str(spec["filename"])).resolve())
            else:
                expected = spec[key]
            if artifact.get(key) != expected:
                raise Blocked("validation", f"wheel artifact {index} has invalid {key}")
        if require_bounded_int(artifact.get("bytes"), int(spec["bytes"]), "wheel bytes") != spec["bytes"]:
            raise Blocked("validation", "wheel byte evidence differs from frozen size")
        member_count = require_bounded_int(
            artifact.get("member_count"), MAX_WHEEL_MEMBERS, "wheel members"
        )
        file_count = require_bounded_int(
            artifact.get("file_member_count"), MAX_WHEEL_MEMBERS, "wheel files"
        )
        directory_count = require_bounded_int(
            artifact.get("directory_count"), MAX_WHEEL_MEMBERS, "wheel directories"
        )
        if (
            member_count != spec["member_count"]
            or file_count != spec["file_member_count"]
            or directory_count != spec["directory_count"]
            or member_count != file_count + directory_count
        ):
            raise Blocked("validation", "wheel member-count evidence drifted")
        expected_file_attributes = [
            list(item) for item in sorted(spec["file_attribute_counts"])
        ]
        expected_directory_attributes = [
            list(item) for item in sorted(spec["directory_attribute_counts"])
        ]
        if artifact.get("file_attribute_counts") != expected_file_attributes:
            raise Blocked("validation", "wheel file-attribute evidence drifted")
        if artifact.get("directory_attribute_counts") != expected_directory_attributes:
            raise Blocked("validation", "wheel directory-attribute evidence drifted")
        require_bounded_int(artifact.get("expanded_bytes"), MAX_TASK_BYTES, "wheel expanded bytes")
        for section_name in ("metadata", "wheel"):
            section = artifact.get(section_name)
            if not isinstance(section, dict):
                raise Blocked("validation", f"missing {section_name} evidence")
            size = require_bounded_int(section.get("bytes"), MIB, section_name + " bytes")
            digest = require_sha256(section.get("sha256"), section_name)
            encoded = section.get("raw_base64")
            if not isinstance(encoded, str):
                raise Blocked("validation", f"missing raw {section_name} bytes")
            try:
                raw = base64.b64decode(encoded, validate=True)
            except Exception as exc:
                raise Blocked("validation", f"invalid raw {section_name} base64") from exc
            if len(raw) != size or sha256_bytes(raw) != digest:
                raise Blocked("validation", f"raw {section_name} bytes/hash mismatch")
            headers = section.get("headers")
            if not isinstance(headers, list) or headers != raw_headers(raw):
                raise Blocked("validation", f"raw {section_name} headers mismatch")
            if section_name == "metadata":
                if message_values(raw, "Name") != [spec["name"]]:
                    raise Blocked("validation", f"wheel artifact {index} Name drifted")
                if message_values(raw, "Version") != [spec["version"]]:
                    raise Blocked("validation", f"wheel artifact {index} Version drifted")
                if message_values(raw, "Requires-Python") != [spec["requires_python"]]:
                    raise Blocked(
                        "validation",
                        f"wheel artifact {index} Requires-Python drifted",
                    )
                if tuple(message_values(raw, "Requires-Dist")) != spec["requires_dist"]:
                    raise Blocked(
                        "validation",
                        f"wheel artifact {index} Requires-Dist drifted",
                    )
            elif message_values(raw, "Tag") != [spec["tag"]]:
                raise Blocked("validation", f"wheel artifact {index} Tag drifted")
        if artifact.get("pep658_metadata_sha256") != spec.get("pep658_sha256"):
            raise Blocked("validation", f"wheel artifact {index} PEP-658 hash drifted")
        record = artifact.get("record")
        if not isinstance(record, dict):
            raise Blocked("validation", "missing RECORD evidence")
        require_bounded_int(record.get("bytes"), MAX_JSON_BYTES, "RECORD bytes")
        require_sha256(record.get("sha256"), "RECORD")
        rows = record.get("rows")
        if not isinstance(rows, list) or len(rows) != file_count:
            raise Blocked("validation", "RECORD/file-member count evidence mismatch")
        file_names: set[str] = set()
        folded: set[str] = set()
        for row in rows:
            if not isinstance(row, list) or len(row) != 3 or not all(isinstance(v, str) for v in row):
                raise Blocked("validation", "invalid RECORD evidence row")
            safe_zip_name(row[0])
            if row[0] in file_names or row[0].casefold() in folded:
                raise Blocked("validation", "duplicate RECORD evidence row")
            file_names.add(row[0])
            folded.add(row[0].casefold())
        directories = artifact.get("directories")
        if not isinstance(directories, list) or len(directories) != directory_count:
            raise Blocked("validation", "directory evidence count mismatch")
        observed_directory_attributes: dict[tuple[int, int, int, int], int] = {}
        for directory in directories:
            if not isinstance(directory, dict) or set(directory) != {
                "name",
                "create_system",
                "external_attr",
                "flag_bits",
                "compress_type",
                "file_size",
                "compress_size",
                "crc",
            }:
                raise Blocked("validation", "invalid directory evidence projection")
            name = directory["name"]
            if not isinstance(name, str) or not name.endswith("/") or name.endswith("//"):
                raise Blocked("validation", "invalid directory evidence name")
            logical_name = name[:-1]
            safe_zip_name(logical_name)
            create_system = require_bounded_int(
                directory["create_system"], 3, "directory create system"
            )
            external_attr = require_bounded_int(
                directory["external_attr"], 0xFFFFFFFF, "directory attributes"
            )
            flag_bits = require_bounded_int(
                directory["flag_bits"], 0xFFFF, "directory flag bits"
            )
            compress_type = require_bounded_int(
                directory["compress_type"], 0xFFFF, "directory compression"
            )
            file_size = require_bounded_int(
                directory["file_size"], MAX_TASK_BYTES, "directory file size"
            )
            compress_size = require_bounded_int(
                directory["compress_size"], MAX_TASK_BYTES, "directory compressed size"
            )
            crc = require_bounded_int(directory["crc"], 0xFFFFFFFF, "directory CRC")
            mode = (external_attr >> 16) & 0xFFFF
            directory_key = (create_system, external_attr, flag_bits, compress_type)
            if (
                logical_name.casefold() in folded
                or directory_key
                not in {tuple(item[:4]) for item in spec["directory_attribute_counts"]}
                or not stat.S_ISDIR(mode)
                or stat.S_ISLNK(mode)
                or (external_attr & 0xFFFF) not in (0, 0x10)
                or any(value != 0 for value in (file_size, compress_size, crc))
            ):
                raise Blocked("validation", "unsafe directory evidence")
            observed_directory_attributes[directory_key] = (
                observed_directory_attributes.get(directory_key, 0) + 1
            )
            folded.add(logical_name.casefold())
        if [
            [*key, count]
            for key, count in sorted(observed_directory_attributes.items())
        ] != expected_directory_attributes:
            raise Blocked("validation", "directory attribute counts do not match entries")
    installed_sections = [wheels.get("installed")]
    if "installed_post_inventory" in wheels:
        installed_sections.append(wheels.get("installed_post_inventory"))
    for installed in installed_sections:
        if not isinstance(installed, dict) or installed.get("status") not in {
            "NOT_RUN",
            "BLOCKED",
            "VERIFIED",
        }:
            raise Blocked("validation", "invalid installed evidence status")
        if installed.get("status") == "VERIFIED":
            distributions = installed.get("distributions")
            if not isinstance(distributions, dict) or set(distributions) != {
                spec["name"] for spec in WHEELS
            }:
                raise Blocked("validation", "verified installed distribution set is not exact")
            expected_versions = {
                str(spec["name"]): str(spec["version"]) for spec in WHEELS
            }
            for distribution_name, expected_version in expected_versions.items():
                summary = distributions.get(distribution_name)
                if (
                    not isinstance(summary, dict)
                    or summary.get("version") != expected_version
                ):
                    raise Blocked(
                        "validation",
                        f"verified installed version is not exact for {distribution_name}",
                    )
            if installed.get("bytecode_paths") != []:
                raise Blocked("validation", "verified installed evidence contains bytecode")
            require_bounded_int(
                installed.get("installed_delta_file_count"),
                MAX_INSTALLED_FILES,
                "installed delta files",
            )


def validate_api_evidence(api: dict[str, object]) -> None:
    if api.get("status") != "PASS":
        return
    if api.get("version_target") != VERSION_TARGET or api.get("version_calls") != 1:
        raise Blocked("validation", "PASS API evidence has invalid version-call record")
    version = api.get("runtime_occt_version")
    if not isinstance(version, str) or re.match(r"^\s*7\.9\.3(?:\D|$)", version) is None:
        raise Blocked("validation", "PASS API evidence has invalid runtime version")
    if api.get("forbidden_modules") != [] or api.get("repo_source_paths") != []:
        raise Blocked("validation", "PASS API evidence violates import isolation")
    ocp_origin = api.get("ocp_origin")
    if not isinstance(ocp_origin, str) or not Path(ocp_origin).resolve().is_relative_to(
        (TASK_ROOT / "venv" / "Lib" / "site-packages").resolve()
    ):
        raise Blocked("validation", "PASS OCP origin is outside isolated site-packages")
    targets = api.get("targets")
    if not isinstance(targets, list) or [item.get("target") for item in targets if isinstance(item, dict)] != list(TARGETS):
        raise Blocked("validation", "API evidence does not contain exact ordered targets")
    conclusions = {"AGREE", "AMBIGUOUS", "MISSING", "CONFLICT"}
    declaration_count = 0
    for item in targets:
        if not isinstance(item, dict) or item.get("conclusion") not in conclusions:
            raise Blocked("validation", "invalid API target conclusion")
        declarations = item.get("declarations")
        if not isinstance(declarations, list):
            raise Blocked("validation", "invalid API target declarations")
        declaration_count += len(declarations)
    if declaration_count > MAX_DECLARATIONS:
        raise Blocked("validation", "API declaration evidence exceeds cap")
    stub_files = api.get("stub_files")
    if not isinstance(stub_files, list) or len(stub_files) > MAX_PYI_FILES:
        raise Blocked("validation", "stub-file evidence exceeds cap")
    if api.get("stub_file_count") != len(stub_files):
        raise Blocked("validation", "stub-file count evidence mismatches")
    aggregate = 0
    stub_provenance: dict[str, str] = {}
    for item in stub_files:
        if not isinstance(item, dict):
            raise Blocked("validation", "invalid stub-file evidence")
        path = item.get("path")
        if not isinstance(path, str) or not path or path in stub_provenance:
            raise Blocked("validation", "invalid/duplicate stub-file path evidence")
        aggregate += require_bounded_int(item.get("bytes"), MAX_PYI_BYTES, "stub bytes")
        stub_provenance[path] = require_sha256(item.get("sha256"), "stub file")
    if aggregate > MAX_PYI_TOTAL or api.get("stub_aggregate_bytes") != aggregate:
        raise Blocked("validation", "stub aggregate evidence exceeds/mismatches cap")
    declaration_bytes = 0
    captured_bytes = 0
    declaration_count = 0
    for target_item in targets:
        declarations = target_item["declarations"]
        for declaration in declarations:
            if not isinstance(declaration, dict):
                raise Blocked("validation", "invalid declaration evidence")
            declaration_count += 1
            path = declaration.get("path")
            if (
                not isinstance(path, str)
                or path not in stub_provenance
                or declaration.get("file_sha256") != stub_provenance[path]
            ):
                raise Blocked("validation", "declaration provenance mismatch")
            line_start = require_bounded_int(
                declaration.get("line_start"),
                MAX_PYI_BYTES,
                "declaration starting line",
            )
            line_end = require_bounded_int(
                declaration.get("line_end"),
                MAX_PYI_BYTES,
                "declaration ending line",
            )
            if line_start < 1 or line_end < line_start:
                raise Blocked("validation", "invalid declaration line extent")
            if declaration.get("kind") not in {
                "FunctionDef",
                "AsyncFunctionDef",
                "ClassDef",
                "Assign",
                "AnnAssign",
            }:
                raise Blocked("validation", "invalid declaration kind")
            source = declaration.get("source")
            if not isinstance(source, str):
                raise Blocked("validation", "invalid declaration source")
            source_bytes = len(source.encode("utf-8"))
            if source_bytes > MAX_DOC_BYTES:
                raise Blocked("validation", "declaration source exceeds per-field cap")
            declaration_bytes += source_bytes
            if declaration_bytes > MAX_DOC_TOTAL:
                raise Blocked("validation", "declaration source aggregate exceeds cap")
        if type(target_item.get("runtime_exists")) is not bool:
            raise Blocked("validation", "target runtime-presence evidence is not boolean")
        if target_item["runtime_exists"]:
            signature = target_item.get("signature")
            if not isinstance(signature, dict) or set(signature) != {"value", "error"}:
                raise Blocked("validation", "invalid signature evidence projection")
            if (signature["value"] is None) == (signature["error"] is None):
                raise Blocked("validation", "signature evidence must contain one value/error")
            selected = signature["value"] if signature["value"] is not None else signature["error"]
            captured_bytes += validate_bounded_text(selected, "signature")
            captured_bytes += validate_bounded_text(
                target_item.get("text_signature"),
                "text signature",
            )
            captured_bytes += validate_bounded_text(target_item.get("doc"), "documentation")
    if declaration_count > MAX_DECLARATIONS:
        raise Blocked("validation", "API declaration evidence exceeds cap")
    if api.get("stub_declaration_bytes") != declaration_bytes:
        raise Blocked("validation", "stub declaration byte count mismatches")
    captured_bytes += declaration_bytes
    if captured_bytes > MAX_DOC_TOTAL or api.get("captured_doc_signature_bytes") != captured_bytes:
        raise Blocked("validation", "captured docs/signatures aggregate mismatches/exceeds cap")


def validate_pending(deadline: float | None = None) -> int:
    if "OCP" in sys.modules:
        raise Blocked("validation", "validator process imported OCP")
    if not PENDING_ROOT.is_dir() or PENDING_ROOT.is_symlink() or PENDING_ROOT.is_junction():
        raise Blocked("validation", "pending root missing/nonregular")
    entries = sorted(PENDING_ROOT.iterdir(), key=lambda path: path.name)
    if [path.name for path in entries] != sorted(EVIDENCE_NAMES):
        raise Blocked("validation", "pending inventory is not exact seven-file set")
    total = 0
    for path in entries:
        check_deadline(deadline, "pending evidence validation")
        if not path.is_file() or path.is_symlink():
            raise Blocked("validation", f"nonregular evidence entry {path.name}")
        total += path.stat().st_size
    if total > MAX_EVIDENCE_BYTES:
        raise Blocked("validation", "pending bundle exceeds evidence cap")
    documents: dict[str, dict[str, object]] = {}
    for name in ("WHEELS.json", "API_INVENTORY.json", "OUTCOME.json"):
        value = load_canonical_json(PENDING_ROOT / name)
        if not isinstance(value, dict) or type(value.get("schema")) is not int or value.get("schema") != 1:
            raise Blocked("validation", f"invalid evidence schema {name}")
        documents[name] = value
    wheels = documents["WHEELS.json"]
    api = documents["API_INVENTORY.json"]
    outcome_document = documents["OUTCOME.json"]
    if wheels.get("status") not in {"NOT_RUN", "BLOCKED", "VERIFIED"}:
        raise Blocked("validation", "invalid WHEELS status")
    if not isinstance(wheels.get("artifacts"), list) or not isinstance(wheels.get("local_sources"), list):
        raise Blocked("validation", "invalid WHEELS result arrays")
    if not isinstance(wheels.get("installed"), dict):
        raise Blocked("validation", "invalid WHEELS installed result")
    if wheels.get("status") == "NOT_RUN" and (
        wheels["artifacts"]
        or wheels["local_sources"]
        or wheels["installed"].get("status") != "NOT_RUN"
    ):
        raise Blocked("validation", "WHEELS NOT_RUN contains attempted-stage evidence")
    if wheels.get("status") == "VERIFIED":
        if len(wheels["artifacts"]) != len(WHEELS) or len(wheels["local_sources"]) != len(WHEELS):
            raise Blocked("validation", "VERIFIED wheel evidence is incomplete")
        if any(
            not isinstance(item, dict) or item.get("status") != "VERIFIED"
            for item in wheels["local_sources"]
        ):
            raise Blocked("validation", "VERIFIED local wheel reuse evidence is incomplete")
    validate_wheel_evidence(wheels, outcome_document.get("first_failure"))
    if api.get("status") not in {"NOT_RUN", "BLOCKED", "PASS"}:
        raise Blocked("validation", "invalid API inventory status")
    if not isinstance(api.get("targets"), list) or not isinstance(api.get("stub_files"), list):
        raise Blocked("validation", "invalid API result arrays")
    if api.get("status") == "NOT_RUN" and (
        api["targets"] or api["stub_files"] or api.get("version_calls") != 0
    ):
        raise Blocked("validation", "API NOT_RUN contains attempted-stage evidence")
    stdout_bytes = (PENDING_ROOT / "STDOUT.txt").read_bytes()
    stderr_bytes = (PENDING_ROOT / "STDERR.txt").read_bytes()
    if api.get("status") == "NOT_RUN" and (stdout_bytes or stderr_bytes):
        raise Blocked("validation", "NOT_RUN inventory has nonempty probe streams")
    if api.get("status") == "PASS":
        if stderr_bytes or canonical_json_bytes(api) != stdout_bytes:
            raise Blocked("validation", "PASS API document does not match clean probe stdout")
    validate_api_evidence(api)
    if outcome_document.get("status") not in {"PASS", "BLOCKED"}:
        raise Blocked("validation", "invalid OUTCOME status")
    if type(outcome_document.get("attempt")) is not int or outcome_document.get("attempt") != 4:
        raise Blocked("validation", "OUTCOME is not recovery attempt 4")
    if canonical_json_bytes(outcome_document.get("attempt_history")) != canonical_json_bytes(
        list(ATTEMPT_HISTORY)
    ):
        raise Blocked("validation", "OUTCOME predecessor attempt history drifted")
    if canonical_json_bytes(outcome_document.get("predecessor_receipt")) != canonical_json_bytes(
        PREDECESSOR_RECEIPT
    ):
        raise Blocked("validation", "OUTCOME predecessor receipt reference drifted")
    secondary_failures = outcome_document.get("secondary_failures")
    if not isinstance(secondary_failures, list) or any(
        not isinstance(item, dict) for item in secondary_failures
    ):
        raise Blocked("validation", "OUTCOME secondary failures are invalid")
    commands = outcome_document.get("commands")
    if not isinstance(commands, list):
        raise Blocked("validation", "OUTCOME commands is not a list")
    attempted_reuse = bool(wheels.get("local_sources"))
    attempted_inventory = bool(api.get("attempted")) or any(
        isinstance(command, dict) and command.get("stage") == "inventory" for command in commands
    )
    if attempted_reuse and wheels.get("status") == "NOT_RUN":
        raise Blocked("validation", "local-reuse attempt was erased as NOT_RUN")
    if attempted_inventory and api.get("status") == "NOT_RUN":
        raise Blocked("validation", "inventory attempt was erased as NOT_RUN")
    if outcome_document.get("status") == "PASS":
        if wheels.get("status") != "VERIFIED" or api.get("status") != "PASS":
            raise Blocked("validation", "PASS outcome lacks verified wheel/API evidence")
        installed = wheels.get("installed")
        installed_post = wheels.get("installed_post_inventory")
        if (
            not isinstance(installed, dict)
            or installed.get("status") != "VERIFIED"
            or not isinstance(installed_post, dict)
            or installed_post.get("status") != "VERIFIED"
        ):
            raise Blocked("validation", "PASS outcome lacks both verified install proofs")
        expected_delta = sorted(str(spec["name"]) for spec in WHEELS)
        if installed.get("delta") != expected_delta:
            raise Blocked("validation", "PASS installed distribution delta is not exact")
        if (
            installed.get("distributions") != installed_post.get("distributions")
            or installed.get("installed_delta_file_count")
            != installed_post.get("installed_delta_file_count")
            or installed.get("baseline_file_count") != installed_post.get("baseline_file_count")
        ):
            raise Blocked("validation", "post-inventory install proof drifted")
        if outcome_document.get("first_failure") is not None:
            raise Blocked("validation", "PASS outcome contains a failure")
        if secondary_failures:
            raise Blocked("validation", "PASS outcome contains secondary failures")
    elif not isinstance(outcome_document.get("first_failure"), dict):
        raise Blocked("validation", "BLOCKED outcome lacks first failure")
    elapsed = outcome_document.get("elapsed_seconds")
    if not isinstance(elapsed, (int, float)) or isinstance(elapsed, bool) or elapsed < 0 or elapsed > TOTAL_SECONDS:
        raise Blocked("validation", "OUTCOME elapsed time exceeds registered wall cap")
    if len(stdout_bytes) > MAX_STREAM_BYTES or len(stderr_bytes) > MAX_STREAM_BYTES:
        raise Blocked("validation", "individual probe stream exceeds cap")
    lines = (PENDING_ROOT / "SHA256SUMS.txt").read_text(encoding="ascii").splitlines()
    if len(lines) != 6:
        raise Blocked("validation", "SHA256SUMS must have six lines")
    parsed: list[tuple[str, int, str]] = []
    for line in lines:
        match = re.fullmatch(r"([0-9a-f]{64})  ([0-9]+)  ([A-Za-z0-9_.-]+)", line)
        if match is None:
            raise Blocked("validation", "invalid SHA256SUMS line")
        parsed.append((match.group(1), int(match.group(2)), match.group(3)))
    if [item[2] for item in parsed] != list(HASHED_EVIDENCE_NAMES):
        raise Blocked("validation", "SHA256SUMS paths are not exact sorted six")
    for expected_hash, expected_size, name in parsed:
        actual_hash, actual_size = sha256_file(
            PENDING_ROOT / name,
            cap=MAX_EVIDENCE_BYTES,
            deadline=deadline,
        )
        if actual_hash != expected_hash or actual_size != expected_size:
            raise Blocked("validation", f"evidence digest mismatch {name}")
    probe_hash, _ = sha256_file(PENDING_ROOT / "PROBE.py")
    outcome = outcome_document
    if outcome.get("probe_sha256") != probe_hash or outcome.get("plan_sha256") != PLAN_SHA256:
        raise Blocked("validation", "probe/plan identity mismatch in OUTCOME")
    return 0


def publish_pending(global_deadline: float) -> None:
    assert kernel32 is not None
    if FINAL_ROOT.exists() or not PENDING_ROOT.is_dir():
        raise Blocked("publication", "publish precondition changed")
    if PENDING_ROOT.parent.resolve() != FINAL_ROOT.parent.resolve():
        raise Blocked("publication", "pending/final are not siblings")
    attributes = os.lstat(PENDING_ROOT)
    if (
        stat.S_ISLNK(attributes.st_mode)
        or not stat.S_ISDIR(attributes.st_mode)
        or PENDING_ROOT.is_junction()
    ):
        raise Blocked("publication", "pending evidence root is a link/non-directory")
    before_identity = (
        attributes.st_dev,
        attributes.st_ino,
        attributes.st_size,
        attributes.st_mtime_ns,
        attributes.st_ctime_ns,
    )
    validate_pending(global_deadline)
    after = os.lstat(PENDING_ROOT)
    after_identity = (
        after.st_dev,
        after.st_ino,
        after.st_size,
        after.st_mtime_ns,
        after.st_ctime_ns,
    )
    if after_identity != before_identity:
        raise Blocked("publication", "pending evidence root changed during final validation")
    if not kernel32.MoveFileExW(str(PENDING_ROOT), str(FINAL_ROOT), MOVEFILE_WRITE_THROUGH):
        raise win_error("MoveFileExW(publish evidence)")
    if not FINAL_ROOT.is_dir() or PENDING_ROOT.exists():
        raise Blocked("publication", "atomic evidence rename did not linearize")


def controller_main(probe: Path) -> int:
    global _FROZEN_PROBE_SHA256
    started_at = utc_now()
    started = time.monotonic()
    global_deadline = started + TOTAL_SECONDS
    operation_deadline = global_deadline - PUBLICATION_RESERVE_SECONDS
    probe_hash, probe_size = sha256_file(probe)
    probe_bytes = probe.read_bytes()
    if len(probe_bytes) != probe_size or sha256_bytes(probe_bytes) != probe_hash:
        raise Blocked("identity", "probe changed during initial freeze read")
    _FROZEN_PROBE_SHA256 = probe_hash
    stdout = b""
    stderr = b""
    wheel_results: list[dict[str, object]] = []
    wheel_document: dict[str, object] = {
        "schema": 1,
        "status": "NOT_RUN",
        "artifacts": [],
        "local_sources": [],
        "installed": {"status": "NOT_RUN", "distributions": {}, "bytecode_paths": []},
    }
    api_document = placeholder_api("NOT_RUN")
    commands: list[dict[str, object]] = []
    failure: dict[str, object] | None = None
    secondary_failures: list[dict[str, str]] = []
    status = "BLOCKED"
    worker_job = None
    venv = TASK_ROOT / "venv"
    wheelhouse = TASK_ROOT / "wheelhouse"
    tmp = TASK_ROOT / "tmp"
    environment = dict(os.environ)
    environment.update(
        {
            "PYTHONPATH": "",
            "PYTHONNOUSERSITE": "1",
            "PYTHONDONTWRITEBYTECODE": "1",
            "PIP_DISABLE_PIP_VERSION_CHECK": "1",
            "PIP_NO_INDEX": "1",
            "PIP_CACHE_DIR": str(tmp / "pip-cache"),
            "TEMP": str(tmp),
            "TMP": str(tmp),
        }
    )
    try:
        if os.name != "nt" or kernel32 is None:
            raise Blocked("preflight", "controller is not running on Windows")
        worker_job = configure_worker_job()
        preflight_controller(probe)
        wheelhouse.mkdir(exist_ok=False)
        tmp.mkdir(exist_ok=False)
        task_tree_bytes()
        foundation_preflight(
            worker_job,
            environment,
            operation_deadline,
            commands,
        )
        exercise_evidence_staging()

        wheel_document["status"] = "BLOCKED"
        reuse_deadline = min(operation_deadline, time.monotonic() + REUSE_SECONDS)
        for spec in WHEELS:
            check_deadline(reuse_deadline, "wheel reuse")
            wheel_path = wheelhouse / str(spec["filename"])
            reuse_record = {
                "stage": "local-reuse:" + str(spec["key"]),
                "method": "LOCAL_REUSE",
                "status": "STARTED",
                "source_path": str((V2_WHEELHOUSE / str(spec["filename"])).resolve()),
                "destination_path": str(wheel_path.resolve()),
                "bytes": None,
                "sha256": None,
                "failure": None,
                "started_at": utc_now(),
                "completed_at": None,
            }
            wheel_document["local_sources"].append(reuse_record)
            try:
                verified_reuse = reuse_wheel(spec, wheel_path, reuse_deadline)
            except BaseException as reuse_error:
                if isinstance(reuse_error, Blocked):
                    message = reuse_error.message
                else:
                    message = f"{type(reuse_error).__name__}: {reuse_error}"
                terminal_failure = {
                    "type": "BLOCKED",
                    "stage": str(reuse_record["stage"]),
                    "message": message,
                }
                reuse_record["status"] = "BLOCKED"
                reuse_record["failure"] = terminal_failure
                reuse_record["completed_at"] = utc_now()
                commands.append(dict(reuse_record))
                raise Blocked(str(reuse_record["stage"]), message) from reuse_error
            reuse_record.update(verified_reuse)
            reuse_record["completed_at"] = utc_now()
            commands.append(dict(reuse_record))
        for spec in WHEELS:
            check_deadline(operation_deadline, "wheel validation")
            result = validate_wheel(
                spec,
                wheelhouse / str(spec["filename"]),
                operation_deadline,
            )
            wheel_results.append(result)
            wheel_document["artifacts"] = list(wheel_results)
        wheel_document["status"] = "VERIFIED"
        task_tree_bytes()

        venv_argv = [str(HOST_PYTHON), "-I", "-B", "-m", "venv", "--copies", str(venv)]
        if sha256_file(probe)[0] != probe_hash:
            raise Blocked("identity", "probe changed before venv child")
        exit_code, child_out, child_err = run_worker(
            worker_job,
            venv_argv,
            cwd=TASK_ROOT,
            environment=environment,
            stage="venv",
            seconds=VENV_SECONDS,
            global_deadline=operation_deadline,
        )
        commands.append({"stage": "venv", "argv": venv_argv, "exit": exit_code})
        if exit_code != 0:
            raise Blocked("venv", f"venv failed: {child_err[-2000:].decode('utf-8', 'replace')}")
        venv_python = venv / "Scripts" / "python.exe"
        if not venv_python.is_file():
            raise Blocked("venv", "venv Python missing")
        wheel_document["venv_baseline_bytecode_cleanup"] = remove_venv_baseline_bytecode(venv)
        site = site_packages(venv)
        baseline = distribution_inventory(site)
        baseline_files = site_tree_snapshot(site, operation_deadline)
        wheel_document["installed"] = {
            "status": "BLOCKED",
            "distributions": {},
            "bytecode_paths": [],
        }
        pip_argv = [
            str(venv_python),
            "-m",
            "pip",
            "install",
            "--disable-pip-version-check",
            "--no-index",
            "--no-deps",
            "--no-cache-dir",
            "--no-compile",
            str(wheelhouse / str(WHEELS[1]["filename"])),
            str(wheelhouse / str(WHEELS[0]["filename"])),
            str(wheelhouse / str(WHEELS[2]["filename"])),
        ]
        if sha256_file(probe)[0] != probe_hash:
            raise Blocked("identity", "probe changed before pip child")
        exit_code, child_out, child_err = run_worker(
            worker_job,
            pip_argv,
            cwd=TASK_ROOT,
            environment=environment,
            stage="pip-install",
            seconds=INSTALL_SECONDS,
            global_deadline=operation_deadline,
        )
        commands.append({"stage": "pip-install", "argv": pip_argv, "exit": exit_code})
        if exit_code != 0:
            raise Blocked("install", f"pip failed: {child_err[-2000:].decode('utf-8', 'replace')}")
        after = distribution_inventory(site)
        delta = sorted(set(after) - set(baseline))
        if delta != sorted(spec["name"] for spec in WHEELS):
            raise Blocked("install", f"installed delta mismatch: {delta}")
        wheel_document["installed"] = verify_installed_files(
            site,
            wheelhouse,
            wheel_results,
            baseline_files,
            operation_deadline,
        )
        wheel_document["installed"]["baseline_distributions"] = baseline
        wheel_document["installed"]["delta"] = delta
        task_tree_bytes()

        inventory_argv = [str(venv_python), "-I", "-B", str(probe), "--inventory"]
        if sha256_file(probe)[0] != probe_hash:
            raise Blocked("identity", "probe changed before inventory child")
        api_document = placeholder_api("BLOCKED")
        api_document["attempted"] = True
        exit_code, stdout, stderr = run_worker(
            worker_job,
            inventory_argv,
            cwd=TASK_ROOT,
            environment=environment,
            stage="inventory",
            seconds=INVENTORY_SECONDS,
            global_deadline=operation_deadline,
        )
        commands.append({"stage": "inventory", "argv": inventory_argv, "exit": exit_code})
        if sha256_file(probe)[0] != probe_hash:
            raise Blocked("identity", "probe changed after inventory child")
        if exit_code != 0:
            raise Blocked("inventory", f"inventory child exited {exit_code}")
        if stderr:
            raise Blocked("inventory", "inventory child emitted stderr")
        try:
            api_document = json.loads(stdout)
        except Exception as exc:
            raise Blocked("inventory", f"inventory stdout is not JSON: {exc}") from exc
        json_depth(api_document)
        if canonical_json_bytes(api_document) != stdout:
            raise Blocked("inventory", "inventory stdout is not canonical JSON")
        if api_document.get("status") != "PASS":
            raise Blocked("inventory", "inventory document did not report PASS")
        wheel_document["installed_post_inventory"] = {
            "status": "BLOCKED",
            "distributions": {},
            "bytecode_paths": [],
        }
        wheel_document["installed_post_inventory"] = verify_installed_files(
            site,
            wheelhouse,
            wheel_results,
            baseline_files,
            operation_deadline,
        )
        task_tree_bytes()
        status = "PASS"
    except Blocked as exc:
        if api_document.get("attempted"):
            stdout = getattr(exc, "captured_stdout", stdout)
            stderr = getattr(exc, "captured_stderr", stderr)
        failure = {"type": "BLOCKED", "stage": exc.stage, "message": exc.message}
        secondary_failures.extend(
            {
                "stage": "worker-cleanup",
                "type": "note",
                "message": note,
            }
            for note in getattr(exc, "__notes__", ())
        )
    except BaseException as exc:
        if api_document.get("attempted"):
            stdout = getattr(exc, "captured_stdout", stdout)
            stderr = getattr(exc, "captured_stderr", stderr)
        failure = {
            "type": type(exc).__module__ + "." + type(exc).__qualname__,
            "stage": "controller",
            "message": str(exc),
            "traceback": "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))[-8192:],
        }
        secondary_failures.extend(
            {
                "stage": "worker-cleanup",
                "type": "note",
                "message": note,
            }
            for note in getattr(exc, "__notes__", ())
        )
    finally:
        if worker_job:
            try:
                terminate_job_and_confirm_empty(
                    worker_job,
                    125,
                    "controller-stage-cleanup",
                    global_deadline,
                )
            except BaseException as cleanup:
                status = "BLOCKED"
                cleanup_text = f"{type(cleanup).__name__}: {cleanup}"
                if failure is None:
                    failure = {
                        "type": "BLOCKED",
                        "stage": "resource",
                        "message": "worker process-tree cleanup failed: " + cleanup_text,
                    }
                else:
                    secondary_failures.append(
                        {
                            "stage": "worker-cleanup",
                            "type": type(cleanup).__module__ + "." + type(cleanup).__qualname__,
                            "message": str(cleanup),
                        }
                    )

    completed_at = utc_now()
    outcome = {
        "schema": 1,
        "attempt": 4,
        "attempt_history": list(ATTEMPT_HISTORY),
        "predecessor_receipt": PREDECESSOR_RECEIPT,
        "status": status,
        "plan_sha256": PLAN_SHA256,
        "probe_sha256": probe_hash,
        "probe_bytes": probe_size,
        "foundation_commit": FOUNDATION_COMMIT,
        "foundation_tree": FOUNDATION_TREE,
        "host": host_facts(),
        "started_at": started_at,
        "completed_at": completed_at,
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "controller_argv": [str(HOST_PYTHON), "-I", str(probe), "--controller"],
        "commands": commands,
        "first_failure": failure,
        "secondary_failures": secondary_failures,
        "nonclaims": [
            "no application/document/reader/tool/setting lifecycle was called",
            "no CAD file or provider capability was exercised",
            "this is one-host inventory evidence, not native correctness or qualification",
        ],
    }
    try:
        publication_deadline = min(global_deadline, time.monotonic() + VALIDATE_SECONDS)
        check_deadline(publication_deadline, "evidence staging")
        task_tree_bytes()
        stage_evidence(
            probe_bytes=probe_bytes,
            wheel_document=wheel_document,
            api_document=api_document,
            outcome=outcome,
            stdout=stdout,
            stderr=stderr,
        )
        validator_argv = [str(HOST_PYTHON), "-I", "-B", str(probe), "--validate-pending"]
        if sha256_file(probe)[0] != probe_hash:
            raise Blocked("identity", "probe changed before validator child")
        if worker_job is None:
            raise Blocked("publication", "worker job unavailable for validator")
        exit_code, validator_out, validator_err = run_worker(
            worker_job,
            validator_argv,
            cwd=TASK_ROOT,
            environment=environment,
            stage="validator-publication",
            seconds=VALIDATE_SECONDS,
            global_deadline=publication_deadline,
        )
        if exit_code != 0 or validator_out or validator_err:
            raise Blocked("publication", f"validator failed exit={exit_code}")
        if sha256_file(probe)[0] != probe_hash:
            raise Blocked("identity", "probe changed after validator child")
        if sha256_file(PENDING_ROOT / "PROBE.py")[0] != probe_hash:
            raise Blocked("identity", "staged PROBE.py differs from frozen probe")
        check_deadline(publication_deadline, "evidence publication")
        if active_job_processes(worker_job) != 0:
            raise Blocked("resource", "validator worker job was not empty before close")
        if not kernel32.CloseHandle(worker_job):
            raise win_error("CloseHandle(empty worker job)")
        worker_job = None
        publish_pending(publication_deadline)
    except BaseException as publication_error:
        if worker_job is not None:
            try:
                terminate_job_and_confirm_empty(
                    worker_job,
                    126,
                    "publication-cleanup",
                    global_deadline,
                )
            except BaseException as cleanup_error:
                publication_error.add_note(
                    "publication worker cleanup also failed: "
                    f"{type(cleanup_error).__name__}: {cleanup_error}"
                )
            finally:
                if not kernel32.CloseHandle(worker_job):
                    publication_error.add_note(
                        "CloseHandle(worker job) also failed with Windows error "
                        f"{ctypes.get_last_error()}"
                    )
                worker_job = None
        if failure is not None:
            preserved = json.dumps(failure, sort_keys=True, separators=(",", ":"))
            raise Blocked(
                "publication",
                "publication failed after preserved first failure "
                f"{preserved}; publication error "
                f"{type(publication_error).__name__}: {publication_error}",
            ) from publication_error
        raise
    _FROZEN_PROBE_SHA256 = None
    if worker_job:
        kernel32.CloseHandle(worker_job)
    print(json.dumps({"status": status, "evidence": str(FINAL_ROOT), "probe_sha256": probe_hash}, sort_keys=True))
    return 0 if status == "PASS" else 2


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(add_help=False)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--controller", action="store_true")
    group.add_argument("--inventory", action="store_true")
    group.add_argument("--validate-pending", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.inventory:
        return inventory_main()
    if args.validate_pending:
        return validate_pending()
    return controller_main(Path(__file__).resolve())


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Blocked as exc:
        print(json.dumps({"status": "BLOCKED", "stage": exc.stage, "message": exc.message}, sort_keys=True), file=sys.stderr)
        raise SystemExit(2)
