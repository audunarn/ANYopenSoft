from __future__ import annotations

import argparse
import ctypes
import hashlib
import json
import msvcrt
import os
import re
import stat
import sys
import threading
import time
from ctypes import wintypes as wt
from datetime import datetime, timezone
from typing import Any, Callable, Iterable, Mapping, Sequence


PACKET_PATH = r"C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_NO_NUMBA_RESIDUAL_PROVIDER_STAGE_C_COMMAND_EVIDENCE_PACKET_V6.md"
EXECUTOR_PATH = r"C:\Github\ANYopenSoft\governance\tools\anysolver_no_numba_residual_stage_c_host_executor.py"
CATALOG_PLAN_PATH = r"C:\Github\ANYopenSoft\governance\plans\ANYSOLVER_STAGE_C_CATALOG_AWARE_C01_CORRECTION_PLAN.md"
V4_MANIFEST_PATH = r"C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_STAGE_C_V4_IMMUTABLE_EVIDENCE_MANIFEST_D58E8106.json"
IDENTITY_LEDGER_PATH = r"C:\Github\ANYopenSoft\governance\evidence\ANYSOLVER_STAGE_C_CATALOG_C01_ACCEPTED_IDENTITY_LEDGER.json"
INTERPRETER_PATH = r"C:\Python\Python313\python.exe"
QUALIFICATION_ROOT = r"C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification\ANYsolver-no-numba-residual-82a9db28"
WSL_PATH = r"C:\WINDOWS\system32\wsl.exe"
KERNEL_PATH = r"C:\WINDOWS\system32\ntoskrnl.exe"
WORKDIR = r"C:\Github\ANYopenSoft"
BOSS_THREAD_ID = "019ff655-abd9-7eb1-b94e-d80252ff9215"
EXPECTED_PYTHON = (3, 13, 9)
EXPECTED_WSL_VERSION = "2.6.1.0"
BUILDER_DISTRO = "ANYsolver-ProviderBuilder-Ubuntu-24.04-82a9db28-v1"
FINAL_DISTRO = "ANYsolver-Ubuntu-24.04-82a9db28"
BUILDER_IMPORT = os.path.join(QUALIFICATION_ROOT, "wsl", BUILDER_DISTRO)
FINAL_IMPORT = os.path.join(QUALIFICATION_ROOT, "wsl", FINAL_DISTRO)
PROVIDER_ARCHIVE = os.path.join(
    QUALIFICATION_ROOT,
    "provider",
    "ANYsolver-Ubuntu-24.04-amd64-82a9db28-v1.tar",
)

CHECKS: tuple[tuple[str, tuple[str, ...], int], ...] = (
    ("C01", (), 30),
    ("C02", (WSL_PATH, "--version"), 30),
    ("C03", (WSL_PATH, "--status"), 45),
    ("C04", (WSL_PATH, "--list", "--verbose"), 45),
    ("C05", (WSL_PATH, "--list", "--quiet"), 45),
)
DEADLINE_SECONDS = 300
FINALIZATION_RESERVE_SECONDS = 60

SCHEMA_INTENT = "anysolver.no_numba_residual.stage_c.campaign_intent/2"
SCHEMA_SNAPSHOT = "anysolver.no_numba_residual.provider_stage_c_host_snapshot/1"
SCHEMA_CHECK = "anysolver.no_numba_residual.provider_stage_c_check/2"
SCHEMA_PROCESS = "anysolver.no_numba_residual.provider_stage_c_process/2"
SCHEMA_JOB = "anysolver.no_numba_residual.provider_stage_c_job_process/1"
SCHEMA_ATTRIBUTES = (
    "anysolver.no_numba_residual.provider_stage_c_creation_attributes/1"
)
SCHEMA_REPORT = "anysolver.no_numba_residual.stage_c.result/2"
SCHEMA_FAILURE = "anysolver.no_numba_residual.stage_c.failure/2"
SCHEMA_GLOBAL_RECEIPT_NODE = (
    "anysolver.no_numba_residual.stage_c.global_receipt_chain_node/1"
)
SCHEMA_REGISTRATION_LOSS_FATAL = (
    "anysolver.no_numba_residual.stage_c.registration_loss_stderr/1"
)
SCHEMA_CONTAINMENT_PROOF_LOSS_FATAL = (
    "anysolver.no_numba_residual.stage_c.containment_proof_loss_stderr/1"
)
SCHEMA_V4_MANIFEST = (
    "anysolver.no_numba_residual.stage_c_v4_immutable_evidence_manifest/2"
)
SCHEMA_IDENTITY_LEDGER = (
    "anysolver.no_numba_residual.stage_c_catalog_c01_identity_ledger/2"
)
SCHEMA_C01_TRUST_INTENT = "anysolver.no_numba_residual.stage_c.c01.trust_intent/1"
SCHEMA_C01_EMBEDDED = "anysolver.no_numba_residual.stage_c.c01.embedded_attempt/1"
SCHEMA_C01_ENUMERATION = (
    "anysolver.no_numba_residual.stage_c.c01.catalog_enumeration/1"
)
SCHEMA_C01_CANDIDATE_INTENT = (
    "anysolver.no_numba_residual.stage_c.c01.candidate_intent/1"
)
SCHEMA_C01_CANDIDATE_RESULT = (
    "anysolver.no_numba_residual.stage_c.c01.candidate_result/1"
)
SCHEMA_C01_CANDIDATE_FAILURE = (
    "anysolver.no_numba_residual.stage_c.c01.candidate_failure/1"
)
SCHEMA_C01_RESULT = "anysolver.no_numba_residual.stage_c.c01.result/1"
SCHEMA_C01_FAILURE = "anysolver.no_numba_residual.stage_c.c01.failure/1"
ACCEPTED_V4_EXECUTOR_SHA256 = "9AA38618802590A8A3C169B8ADFFFCA967DF3B3485320CEE16DCA431FC18FC4D"
ACCEPTED_CATALOG_PLAN_SHA256 = "D5FBB6527192026CA6923751B16E96731786AAFE1CC9C37CEBCE8820C49EE88E"
IMMUTABLE_V4_EVIDENCE_ROOT = (
    r"C:\Users\AudunArnesenNyhus\AppData\Local\ANYrelease\qualification"
    r"\ANYsolver-no-numba-residual-82a9db28\provider-stage-c-dc0e416339ccf5bb"
)
SCHEMA_INTERPRETER = (
    "anysolver.no_numba_residual.windows_interpreter_identity/1"
)
SCHEMA_AUTHORITY = (
    "anysolver.no_numba_residual.external_boss_stage_c_execution_authority/1"
)
SCHEMA_PERF_STATE = "anysolver.no_numba_residual.ecosystem_perf_lease_state/1"


class StageCError(RuntimeError):
    pass


class _AtomicJsonPrePromotionFailure(StageCError):
    """An atomic JSON write failed before a final path became durable."""

    def __init__(self, final_path: str, cause: BaseException) -> None:
        super().__init__(f"atomic JSON promotion failed before finalization: {final_path}: {cause}")
        self.final_path = final_path
        self.partial_path = final_path + ".partial"
        self.failing_site = _prejob_site_for_path(final_path)
        self.cause_type = type(cause).__name__
        self.cause_message_sha256 = hashlib.sha256(str(cause).encode("utf-8")).hexdigest()


class _ReceiptRegistrationLost(StageCError):
    """A durable final exists but could not be registered in its receipt chain."""

    exit_code = 86

    def __init__(
        self,
        *,
        phase: str,
        promoted_receipt: Mapping[str, Any],
        prior_receipt: Mapping[str, Any] | None,
        cause: BaseException,
        containment: Mapping[str, Any] | None = None,
        run_id: str | None = None,
        attempted_consumer_id: str | None = None,
        attempt_id: str | None = None,
        durable_head: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(f"durable receipt registration lost in {phase}: {cause}")
        self.phase = phase
        self.promoted_receipt = dict(promoted_receipt)
        self.prior_receipt = None if prior_receipt is None else dict(prior_receipt)
        self.cause_type = type(cause).__name__
        self.cause_message_sha256 = hashlib.sha256(str(cause).encode("utf-8")).hexdigest()
        self.containment = None if containment is None else dict(containment)
        self.run_id = run_id
        self.attempted_consumer_id = attempted_consumer_id
        self.attempt_id = attempt_id
        self.durable_head = (
            None
            if durable_head is None and prior_receipt is None
            else dict(prior_receipt if durable_head is None else durable_head)
        )


class _ContainmentProofLost(StageCError):
    """A child outcome exists but its one-time containment proof is unavailable."""

    exit_code = 87

    def __init__(
        self,
        *,
        phase: str,
        run_id: str,
        durable_head: Mapping[str, Any] | None,
        promoted_receipt: Mapping[str, Any] | None,
        cause: BaseException,
        containment: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(f"containment proof lost in {phase}: {cause}")
        self.phase = phase
        self.run_id = run_id
        self.durable_head = None if durable_head is None else dict(durable_head)
        self.promoted_receipt = None if promoted_receipt is None else dict(promoted_receipt)
        self.cause_type = type(cause).__name__
        self.cause_message_sha256 = hashlib.sha256(str(cause).encode("utf-8")).hexdigest()
        self.containment = None if containment is None else dict(containment)


class _PreJobOrdinaryFailureRouted(StageCError):
    """Marks an ordinary pre-Job failure whose two terminal receipts were emitted."""


class _PreJobOrdinaryFailureContext(dict[str, Any]):
    """Frozen host transport for one ordinary failure before Job creation."""


class _PendingStageCOutcome(dict[str, Any]):
    """Selected campaign outcome retained until the hold finalizer completes."""


class _CampaignWslHoldReleaseOutcome(dict[str, Any]):
    """Non-overriding all-outcome record for the campaign hold finalizer."""


def _prejob_site_for_path(path: str) -> str:
    name = os.path.basename(path).casefold()
    if name == "job_intent.json":
        return "job_intent"
    if name == "creation_attributes_intent.json":
        return "creation_attributes_intent"
    return "atomic_json"


def _utc() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace(
        "+00:00", "Z"
    )


def _error_record(exc: BaseException) -> dict[str, Any]:
    """Return a bounded, deterministic error identity without losing auxiliaries."""

    message = str(exc)
    record: dict[str, Any] = {
        "type": type(exc).__name__,
        "message": message,
        "message_sha256": hashlib.sha256(message.encode("utf-8")).hexdigest(),
    }
    for name in (
        "phase",
        "failing_site",
        "cause_type",
        "cause_message_sha256",
        "catalog_hash_restore_error",
        "catalog_hash_position_error",
        "catalog_hash_evidence",
        "catalog_enumeration_evidence",
        "catalog_enumeration_release_error",
        "catalog_cleanup_errors",
        "c01_failure_receipt_error",
        "held_direct_proof",
    ):
        if hasattr(exc, name):
            record[name] = getattr(exc, name)
    if hasattr(exc, "wintrust_attempt"):
        record["wintrust_attempt"] = getattr(exc, "wintrust_attempt")
    if hasattr(exc, "secondary_errors"):
        record["secondary_errors"] = list(getattr(exc, "secondary_errors"))
    return record


def _norm(path: str) -> str:
    return os.path.normcase(os.path.abspath(path))


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def _sha256_file(path: str) -> tuple[int, str]:
    digest = hashlib.sha256()
    size = 0
    with open(path, "rb", buffering=0) as stream:
        while True:
            block = stream.read(1024 * 1024)
            if not block:
                break
            size += len(block)
            digest.update(block)
    return size, digest.hexdigest().upper()


def _validate_json_value(value: Any, where: str = "$") -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        raise StageCError(f"floating-point JSON value is forbidden at {where}")
    if isinstance(value, list):
        for index, item in enumerate(value):
            _validate_json_value(item, f"{where}[{index}]")
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise StageCError(f"non-string JSON key at {where}")
            _validate_json_value(item, f"{where}.{key}")
        return
    raise StageCError(f"unsupported JSON value {type(value).__name__} at {where}")


def _canonical_json(value: Any) -> bytes:
    _validate_json_value(value)
    return (
        json.dumps(
            value,
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
        + b"\n"
    )


def _read_canonical_receipt(
    path: str, expected_sha256: str, expected_schema: str
) -> tuple[dict[str, Any], dict[str, Any]]:
    with open(path, "rb") as stream:
        raw = stream.read()
    actual_hash = _sha256_bytes(raw)
    if actual_hash != expected_sha256.upper():
        raise StageCError(
            f"receipt hash mismatch for {path}: {actual_hash} != {expected_sha256}"
        )
    if raw.startswith(b"\xef\xbb\xbf"):
        raise StageCError(f"receipt has UTF-8 BOM: {path}")
    try:
        value = json.loads(raw.decode("utf-8-sig"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise StageCError(f"invalid receipt JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise StageCError(f"receipt is not an object: {path}")
    if value.get("schema") != expected_schema:
        raise StageCError(
            f"receipt schema mismatch for {path}: {value.get('schema')!r}"
        )
    if _canonical_json(value) != raw:
        raise StageCError(f"receipt is not canonical UTF-8/LF JSON: {path}")
    return value, {"path": path, "bytes": len(raw), "sha256": actual_hash}


kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
advapi32 = ctypes.WinDLL("advapi32", use_last_error=True)
version_dll = ctypes.WinDLL("version", use_last_error=True)
ntdll = ctypes.WinDLL("ntdll", use_last_error=True)
wintrust = ctypes.WinDLL("wintrust", use_last_error=True)
crypt32 = ctypes.WinDLL("crypt32", use_last_error=True)
psapi = ctypes.WinDLL("psapi", use_last_error=True)

LPBYTE = ctypes.POINTER(wt.BYTE)
ULONG_PTR = ctypes.c_size_t
SIZE_T = ctypes.c_size_t
INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value

ERROR_FILE_NOT_FOUND = 2
ERROR_PATH_NOT_FOUND = 3
ERROR_INSUFFICIENT_BUFFER = 122
ERROR_SERVICE_DOES_NOT_EXIST = 1060
FILE_ATTRIBUTE_DIRECTORY = 0x00000010
FILE_ATTRIBUTE_ARCHIVE = 0x00000020
FILE_ATTRIBUTE_REPARSE_POINT = 0x00000400
INVALID_FILE_ATTRIBUTES = 0xFFFFFFFF
GENERIC_READ = 0x80000000
FILE_READ_ATTRIBUTES = 0x00000080
FILE_SHARE_READ = 0x00000001
FILE_SHARE_WRITE = 0x00000002
FILE_SHARE_DELETE = 0x00000004
OPEN_EXISTING = 3
CREATE_NEW = 1
FILE_FLAG_WRITE_THROUGH = 0x80000000
FILE_FLAG_OPEN_REPARSE_POINT = 0x00200000
FILE_FLAG_BACKUP_SEMANTICS = 0x02000000
MOVEFILE_WRITE_THROUGH = 0x00000008
HANDLE_FLAG_INHERIT = 0x00000001
STARTF_USESTDHANDLES = 0x00000100
CREATE_SUSPENDED = 0x00000004
CREATE_NEW_PROCESS_GROUP = 0x00000200
CREATE_UNICODE_ENVIRONMENT = 0x00000400
EXTENDED_STARTUPINFO_PRESENT = 0x00080000
WAIT_OBJECT_0 = 0
WAIT_TIMEOUT = 258
INFINITE = 0xFFFFFFFF
STILL_ACTIVE = 259
PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
SYNCHRONIZE = 0x00100000
TH32CS_SNAPPROCESS = 0x00000002
JOB_OBJECT_LIMIT_ACTIVE_PROCESS = 0x00000008
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 0x00002000
JOB_OBJECT_EXTENDED_LIMIT_INFORMATION = 9
JOB_OBJECT_BASIC_PROCESS_ID_LIST = 3
PROC_THREAD_ATTRIBUTE_HANDLE_LIST = 0x00020002
PROC_THREAD_ATTRIBUTE_JOB_LIST = 0x0002000D
DUPLICATE_SAME_ACCESS = 0x00000002
MAX_COMBINED_RESIDENT_BYTES = 500 * 1024 * 1024
FILE_BEGIN = 0
FILE_CURRENT = 1
PROCESS_COMMAND_LINE_INFORMATION = 60


class SECURITY_ATTRIBUTES(ctypes.Structure):
    _fields_ = [
        ("nLength", wt.DWORD),
        ("lpSecurityDescriptor", wt.LPVOID),
        ("bInheritHandle", wt.BOOL),
    ]


class BY_HANDLE_FILE_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("dwFileAttributes", wt.DWORD),
        ("ftCreationTime", wt.FILETIME),
        ("ftLastAccessTime", wt.FILETIME),
        ("ftLastWriteTime", wt.FILETIME),
        ("dwVolumeSerialNumber", wt.DWORD),
        ("nFileSizeHigh", wt.DWORD),
        ("nFileSizeLow", wt.DWORD),
        ("nNumberOfLinks", wt.DWORD),
        ("nFileIndexHigh", wt.DWORD),
        ("nFileIndexLow", wt.DWORD),
    ]


class FILE_ID_128(ctypes.Structure):
    _fields_ = [("Identifier", wt.BYTE * 16)]


class FILE_ID_INFO(ctypes.Structure):
    _fields_ = [
        ("VolumeSerialNumber", ctypes.c_ulonglong),
        ("FileId", FILE_ID_128),
    ]


class VS_FIXEDFILEINFO(ctypes.Structure):
    _fields_ = [
        ("dwSignature", wt.DWORD),
        ("dwStrucVersion", wt.DWORD),
        ("dwFileVersionMS", wt.DWORD),
        ("dwFileVersionLS", wt.DWORD),
        ("dwProductVersionMS", wt.DWORD),
        ("dwProductVersionLS", wt.DWORD),
        ("dwFileFlagsMask", wt.DWORD),
        ("dwFileFlags", wt.DWORD),
        ("dwFileOS", wt.DWORD),
        ("dwFileType", wt.DWORD),
        ("dwFileSubtype", wt.DWORD),
        ("dwFileDateMS", wt.DWORD),
        ("dwFileDateLS", wt.DWORD),
    ]


class RTL_OSVERSIONINFOEXW(ctypes.Structure):
    _fields_ = [
        ("dwOSVersionInfoSize", wt.DWORD),
        ("dwMajorVersion", wt.DWORD),
        ("dwMinorVersion", wt.DWORD),
        ("dwBuildNumber", wt.DWORD),
        ("dwPlatformId", wt.DWORD),
        ("szCSDVersion", wt.WCHAR * 128),
        ("wServicePackMajor", wt.WORD),
        ("wServicePackMinor", wt.WORD),
        ("wSuiteMask", wt.WORD),
        ("wProductType", wt.BYTE),
        ("wReserved", wt.BYTE),
    ]


class _SYSTEM_INFO_ARCH(ctypes.Structure):
    _fields_ = [("wProcessorArchitecture", wt.WORD), ("wReserved", wt.WORD)]


class _SYSTEM_INFO_UNION(ctypes.Union):
    _fields_ = [("dwOemId", wt.DWORD), ("arch", _SYSTEM_INFO_ARCH)]


class SYSTEM_INFO(ctypes.Structure):
    _anonymous_ = ("u",)
    _fields_ = [
        ("u", _SYSTEM_INFO_UNION),
        ("dwPageSize", wt.DWORD),
        ("lpMinimumApplicationAddress", wt.LPVOID),
        ("lpMaximumApplicationAddress", wt.LPVOID),
        ("dwActiveProcessorMask", ULONG_PTR),
        ("dwNumberOfProcessors", wt.DWORD),
        ("dwProcessorType", wt.DWORD),
        ("dwAllocationGranularity", wt.DWORD),
        ("wProcessorLevel", wt.WORD),
        ("wProcessorRevision", wt.WORD),
    ]


class PROCESSENTRY32W(ctypes.Structure):
    _fields_ = [
        ("dwSize", wt.DWORD),
        ("cntUsage", wt.DWORD),
        ("th32ProcessID", wt.DWORD),
        ("th32DefaultHeapID", ULONG_PTR),
        ("th32ModuleID", wt.DWORD),
        ("cntThreads", wt.DWORD),
        ("th32ParentProcessID", wt.DWORD),
        ("pcPriClassBase", wt.LONG),
        ("dwFlags", wt.DWORD),
        ("szExeFile", wt.WCHAR * 260),
    ]


class SERVICE_STATUS_PROCESS(ctypes.Structure):
    _fields_ = [
        ("dwServiceType", wt.DWORD),
        ("dwCurrentState", wt.DWORD),
        ("dwControlsAccepted", wt.DWORD),
        ("dwWin32ExitCode", wt.DWORD),
        ("dwServiceSpecificExitCode", wt.DWORD),
        ("dwCheckPoint", wt.DWORD),
        ("dwWaitHint", wt.DWORD),
        ("dwProcessId", wt.DWORD),
        ("dwServiceFlags", wt.DWORD),
    ]


class QUERY_SERVICE_CONFIGW(ctypes.Structure):
    _fields_ = [
        ("dwServiceType", wt.DWORD),
        ("dwStartType", wt.DWORD),
        ("dwErrorControl", wt.DWORD),
        ("lpBinaryPathName", wt.LPWSTR),
        ("lpLoadOrderGroup", wt.LPWSTR),
        ("dwTagId", wt.DWORD),
        ("lpDependencies", wt.LPWSTR),
        ("lpServiceStartName", wt.LPWSTR),
        ("lpDisplayName", wt.LPWSTR),
    ]


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
        ("PerProcessUserTimeLimit", ctypes.c_longlong),
        ("PerJobUserTimeLimit", ctypes.c_longlong),
        ("LimitFlags", wt.DWORD),
        ("MinimumWorkingSetSize", SIZE_T),
        ("MaximumWorkingSetSize", SIZE_T),
        ("ActiveProcessLimit", wt.DWORD),
        ("Affinity", ULONG_PTR),
        ("PriorityClass", wt.DWORD),
        ("SchedulingClass", wt.DWORD),
    ]


class JOBOBJECT_EXTENDED_LIMIT_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("BasicLimitInformation", JOBOBJECT_BASIC_LIMIT_INFORMATION),
        ("IoInfo", IO_COUNTERS),
        ("ProcessMemoryLimit", SIZE_T),
        ("JobMemoryLimit", SIZE_T),
        ("PeakProcessMemoryUsed", SIZE_T),
        ("PeakJobMemoryUsed", SIZE_T),
    ]


class STARTUPINFOW(ctypes.Structure):
    _fields_ = [
        ("cb", wt.DWORD),
        ("lpReserved", wt.LPWSTR),
        ("lpDesktop", wt.LPWSTR),
        ("lpTitle", wt.LPWSTR),
        ("dwX", wt.DWORD),
        ("dwY", wt.DWORD),
        ("dwXSize", wt.DWORD),
        ("dwYSize", wt.DWORD),
        ("dwXCountChars", wt.DWORD),
        ("dwYCountChars", wt.DWORD),
        ("dwFillAttribute", wt.DWORD),
        ("dwFlags", wt.DWORD),
        ("wShowWindow", wt.WORD),
        ("cbReserved2", wt.WORD),
        ("lpReserved2", LPBYTE),
        ("hStdInput", wt.HANDLE),
        ("hStdOutput", wt.HANDLE),
        ("hStdError", wt.HANDLE),
    ]


class STARTUPINFOEXW(ctypes.Structure):
    _fields_ = [("StartupInfo", STARTUPINFOW), ("lpAttributeList", wt.LPVOID)]


class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("hProcess", wt.HANDLE),
        ("hThread", wt.HANDLE),
        ("dwProcessId", wt.DWORD),
        ("dwThreadId", wt.DWORD),
    ]


class PROCESS_MEMORY_COUNTERS_EX(ctypes.Structure):
    _fields_ = [
        ("cb", wt.DWORD),
        ("PageFaultCount", wt.DWORD),
        ("PeakWorkingSetSize", SIZE_T),
        ("WorkingSetSize", SIZE_T),
        ("QuotaPeakPagedPoolUsage", SIZE_T),
        ("QuotaPagedPoolUsage", SIZE_T),
        ("QuotaPeakNonPagedPoolUsage", SIZE_T),
        ("QuotaNonPagedPoolUsage", SIZE_T),
        ("PagefileUsage", SIZE_T),
        ("PeakPagefileUsage", SIZE_T),
        ("PrivateUsage", SIZE_T),
    ]


class UNICODE_STRING(ctypes.Structure):
    _fields_ = [
        ("Length", wt.USHORT),
        ("MaximumLength", wt.USHORT),
        ("Buffer", wt.LPWSTR),
    ]


class GUID(ctypes.Structure):
    _fields_ = [
        ("Data1", wt.DWORD),
        ("Data2", wt.WORD),
        ("Data3", wt.WORD),
        ("Data4", wt.BYTE * 8),
    ]

    @classmethod
    def parse(cls, text: str) -> "GUID":
        import uuid

        raw = uuid.UUID(text).bytes_le
        result = cls()
        ctypes.memmove(ctypes.byref(result), raw, 16)
        return result


class WINTRUST_FILE_INFO(ctypes.Structure):
    _fields_ = [
        ("cbStruct", wt.DWORD),
        ("pcwszFilePath", wt.LPCWSTR),
        ("hFile", wt.HANDLE),
        ("pgKnownSubject", ctypes.POINTER(GUID)),
    ]


class CATALOG_INFO(ctypes.Structure):
    _fields_ = [
        ("cbStruct", wt.DWORD),
        ("wszCatalogFile", wt.WCHAR * 260),
    ]


class WINTRUST_CATALOG_INFO(ctypes.Structure):
    _fields_ = [
        ("cbStruct", wt.DWORD),
        ("dwCatalogVersion", wt.DWORD),
        ("pcwszCatalogFilePath", wt.LPCWSTR),
        ("pcwszMemberTag", wt.LPCWSTR),
        ("pcwszMemberFilePath", wt.LPCWSTR),
        ("hMemberFile", wt.HANDLE),
        ("pbCalculatedFileHash", ctypes.POINTER(ctypes.c_ubyte)),
        ("cbCalculatedFileHash", wt.DWORD),
        ("pcCatalogContext", ctypes.c_void_p),
        ("hCatAdmin", wt.HANDLE),
    ]


class _WINTRUST_UNION(ctypes.Union):
    _fields_ = [
        ("pFile", ctypes.POINTER(WINTRUST_FILE_INFO)),
        ("pCatalog", ctypes.POINTER(WINTRUST_CATALOG_INFO)),
        ("pData", wt.LPVOID),
    ]


class WINTRUST_DATA(ctypes.Structure):
    _anonymous_ = ("u",)
    _fields_ = [
        ("cbStruct", wt.DWORD),
        ("pPolicyCallbackData", wt.LPVOID),
        ("pSIPClientData", wt.LPVOID),
        ("dwUIChoice", wt.DWORD),
        ("fdwRevocationChecks", wt.DWORD),
        ("dwUnionChoice", wt.DWORD),
        ("u", _WINTRUST_UNION),
        ("dwStateAction", wt.DWORD),
        ("hWVTStateData", wt.HANDLE),
        ("pwszURLReference", wt.LPCWSTR),
        ("dwProvFlags", wt.DWORD),
        ("dwUIContext", wt.DWORD),
        ("pSignatureSettings", wt.LPVOID),
    ]


class CRYPT_DATA_BLOB(ctypes.Structure):
    _fields_ = [("cbData", wt.DWORD), ("pbData", LPBYTE)]


class CRYPT_BIT_BLOB(ctypes.Structure):
    _fields_ = [
        ("cbData", wt.DWORD),
        ("pbData", LPBYTE),
        ("cUnusedBits", wt.DWORD),
    ]


class CRYPT_ALGORITHM_IDENTIFIER(ctypes.Structure):
    _fields_ = [("pszObjId", ctypes.c_char_p), ("Parameters", CRYPT_DATA_BLOB)]


class CERT_PUBLIC_KEY_INFO(ctypes.Structure):
    _fields_ = [
        ("Algorithm", CRYPT_ALGORITHM_IDENTIFIER),
        ("PublicKey", CRYPT_BIT_BLOB),
    ]


class CERT_EXTENSION(ctypes.Structure):
    _fields_ = [
        ("pszObjId", ctypes.c_char_p),
        ("fCritical", wt.BOOL),
        ("Value", CRYPT_DATA_BLOB),
    ]


class CERT_INFO(ctypes.Structure):
    _fields_ = [
        ("dwVersion", wt.DWORD),
        ("SerialNumber", CRYPT_DATA_BLOB),
        ("SignatureAlgorithm", CRYPT_ALGORITHM_IDENTIFIER),
        ("Issuer", CRYPT_DATA_BLOB),
        ("NotBefore", wt.FILETIME),
        ("NotAfter", wt.FILETIME),
        ("Subject", CRYPT_DATA_BLOB),
        ("SubjectPublicKeyInfo", CERT_PUBLIC_KEY_INFO),
        ("IssuerUniqueId", CRYPT_BIT_BLOB),
        ("SubjectUniqueId", CRYPT_BIT_BLOB),
        ("cExtension", wt.DWORD),
        ("rgExtension", ctypes.POINTER(CERT_EXTENSION)),
    ]


class CERT_CONTEXT(ctypes.Structure):
    _fields_ = [
        ("dwCertEncodingType", wt.DWORD),
        ("pbCertEncoded", LPBYTE),
        ("cbCertEncoded", wt.DWORD),
        ("pCertInfo", ctypes.POINTER(CERT_INFO)),
        ("hCertStore", wt.HANDLE),
    ]


class CERT_TRUST_STATUS(ctypes.Structure):
    _fields_ = [("dwErrorStatus", wt.DWORD), ("dwInfoStatus", wt.DWORD)]


class CERT_CHAIN_CONTEXT(ctypes.Structure):
    _fields_ = [
        ("cbSize", wt.DWORD),
        ("TrustStatus", CERT_TRUST_STATUS),
        ("cChain", wt.DWORD),
        ("rgpChain", wt.LPVOID),
        ("cLowerQualityChainContext", wt.DWORD),
        ("rgpLowerQualityChainContext", wt.LPVOID),
        ("fHasRevocationFreshnessTime", wt.BOOL),
        ("dwRevocationFreshnessTime", wt.DWORD),
        ("dwCreateFlags", wt.DWORD),
        ("ChainId", GUID),
    ]


class CRYPT_PROVIDER_CERT(ctypes.Structure):
    _fields_ = [
        ("cbStruct", wt.DWORD),
        ("pCert", ctypes.POINTER(CERT_CONTEXT)),
        ("fCommercial", wt.BOOL),
        ("fTrustedRoot", wt.BOOL),
        ("fSelfSigned", wt.BOOL),
        ("fTestCert", wt.BOOL),
        ("dwRevokedReason", wt.DWORD),
        ("dwConfidence", wt.DWORD),
        ("dwError", wt.DWORD),
        ("pTrustListContext", wt.LPVOID),
        ("fTrustListSignerCert", wt.BOOL),
        ("pCtlContext", wt.LPVOID),
        ("dwCtlError", wt.DWORD),
        ("fIsCyclic", wt.BOOL),
        ("pChainElement", wt.LPVOID),
    ]


class CRYPT_PROVIDER_SGNR(ctypes.Structure):
    pass


CRYPT_PROVIDER_SGNR._fields_ = [
    ("cbStruct", wt.DWORD),
    ("sftVerifyAsOf", wt.FILETIME),
    ("csCertChain", wt.DWORD),
    ("pasCertChain", ctypes.POINTER(CRYPT_PROVIDER_CERT)),
    ("dwSignerType", wt.DWORD),
    ("psSigner", wt.LPVOID),
    ("dwError", wt.DWORD),
    ("csCounterSigners", wt.DWORD),
    ("pasCounterSigners", ctypes.POINTER(CRYPT_PROVIDER_SGNR)),
    ("pChainContext", ctypes.POINTER(CERT_CHAIN_CONTEXT)),
]


class CRYPT_PROVIDER_DATA(ctypes.Structure):
    """Prefix of CRYPT_PROVIDER_DATA through the signer array.

    WTHelperProvDataFromStateData owns the returned allocation.  This prefix is
    the documented ABI portion needed to read csSigners/pasSigners; no field
    beyond pasSigners is dereferenced here.
    """

    _fields_ = [
        ("cbStruct", wt.DWORD),
        ("pWintrustData", ctypes.POINTER(WINTRUST_DATA)),
        ("fOpenedFile", wt.BOOL),
        ("hWndParent", wt.HWND),
        ("pgActionID", ctypes.POINTER(GUID)),
        ("hProv", ctypes.c_size_t),
        ("dwError", wt.DWORD),
        ("dwRegSecuritySettings", wt.DWORD),
        ("dwRegPolicySettings", wt.DWORD),
        ("psPfns", wt.LPVOID),
        ("cdwTrustStepErrors", wt.DWORD),
        ("padwTrustStepErrors", ctypes.POINTER(wt.DWORD)),
        ("chStores", wt.DWORD),
        ("pahStores", ctypes.POINTER(wt.HANDLE)),
        ("dwEncoding", wt.DWORD),
        ("hMsg", wt.HANDLE),
        ("csSigners", wt.DWORD),
        ("pasSigners", ctypes.POINTER(CRYPT_PROVIDER_SGNR)),
    ]


class CERT_ENHKEY_USAGE(ctypes.Structure):
    _fields_ = [
        ("cUsageIdentifier", wt.DWORD),
        ("rgpszUsageIdentifier", ctypes.POINTER(ctypes.c_char_p)),
    ]


def _configure_apis() -> None:
    kernel32.GetFileAttributesW.argtypes = [wt.LPCWSTR]
    kernel32.GetFileAttributesW.restype = ctypes.c_uint32
    kernel32.CreateFileW.argtypes = [
        wt.LPCWSTR,
        wt.DWORD,
        wt.DWORD,
        ctypes.POINTER(SECURITY_ATTRIBUTES),
        wt.DWORD,
        wt.DWORD,
        wt.HANDLE,
    ]
    kernel32.CreateFileW.restype = wt.HANDLE
    kernel32.GetFileInformationByHandle.argtypes = [
        wt.HANDLE,
        ctypes.POINTER(BY_HANDLE_FILE_INFORMATION),
    ]
    kernel32.GetFileInformationByHandle.restype = wt.BOOL
    kernel32.GetFileInformationByHandleEx.argtypes = [
        wt.HANDLE,
        ctypes.c_int,
        wt.LPVOID,
        wt.DWORD,
    ]
    kernel32.GetFileInformationByHandleEx.restype = wt.BOOL
    kernel32.CloseHandle.argtypes = [wt.HANDLE]
    kernel32.CloseHandle.restype = wt.BOOL
    kernel32.MoveFileExW.argtypes = [wt.LPCWSTR, wt.LPCWSTR, wt.DWORD]
    kernel32.MoveFileExW.restype = wt.BOOL
    kernel32.FlushFileBuffers.argtypes = [wt.HANDLE]
    kernel32.FlushFileBuffers.restype = wt.BOOL
    kernel32.GetHandleInformation.argtypes = [wt.HANDLE, ctypes.POINTER(wt.DWORD)]
    kernel32.GetHandleInformation.restype = wt.BOOL
    kernel32.SetHandleInformation.argtypes = [wt.HANDLE, wt.DWORD, wt.DWORD]
    kernel32.SetHandleInformation.restype = wt.BOOL
    kernel32.CreateJobObjectW.argtypes = [ctypes.POINTER(SECURITY_ATTRIBUTES), wt.LPCWSTR]
    kernel32.CreateJobObjectW.restype = wt.HANDLE
    kernel32.SetInformationJobObject.argtypes = [wt.HANDLE, ctypes.c_int, wt.LPVOID, wt.DWORD]
    kernel32.SetInformationJobObject.restype = wt.BOOL
    kernel32.QueryInformationJobObject.argtypes = [
        wt.HANDLE,
        ctypes.c_int,
        wt.LPVOID,
        wt.DWORD,
        ctypes.POINTER(wt.DWORD),
    ]
    kernel32.QueryInformationJobObject.restype = wt.BOOL
    kernel32.InitializeProcThreadAttributeList.argtypes = [
        wt.LPVOID,
        wt.DWORD,
        wt.DWORD,
        ctypes.POINTER(SIZE_T),
    ]
    kernel32.InitializeProcThreadAttributeList.restype = wt.BOOL
    kernel32.UpdateProcThreadAttribute.argtypes = [
        wt.LPVOID,
        wt.DWORD,
        SIZE_T,
        wt.LPVOID,
        SIZE_T,
        wt.LPVOID,
        ctypes.POINTER(SIZE_T),
    ]
    kernel32.UpdateProcThreadAttribute.restype = wt.BOOL
    kernel32.DeleteProcThreadAttributeList.argtypes = [wt.LPVOID]
    kernel32.CreateProcessW.argtypes = [
        wt.LPCWSTR,
        wt.LPWSTR,
        ctypes.POINTER(SECURITY_ATTRIBUTES),
        ctypes.POINTER(SECURITY_ATTRIBUTES),
        wt.BOOL,
        wt.DWORD,
        wt.LPVOID,
        wt.LPCWSTR,
        ctypes.POINTER(STARTUPINFOW),
        ctypes.POINTER(PROCESS_INFORMATION),
    ]
    kernel32.CreateProcessW.restype = wt.BOOL
    kernel32.ResumeThread.argtypes = [wt.HANDLE]
    kernel32.ResumeThread.restype = wt.DWORD
    kernel32.WaitForSingleObject.argtypes = [wt.HANDLE, wt.DWORD]
    kernel32.WaitForSingleObject.restype = wt.DWORD
    kernel32.GetExitCodeProcess.argtypes = [wt.HANDLE, ctypes.POINTER(wt.DWORD)]
    kernel32.GetExitCodeProcess.restype = wt.BOOL
    kernel32.TerminateJobObject.argtypes = [wt.HANDLE, wt.UINT]
    kernel32.TerminateJobObject.restype = wt.BOOL
    kernel32.TerminateProcess.argtypes = [wt.HANDLE, wt.UINT]
    kernel32.TerminateProcess.restype = wt.BOOL
    kernel32.OpenProcess.argtypes = [wt.DWORD, wt.BOOL, wt.DWORD]
    kernel32.OpenProcess.restype = wt.HANDLE
    kernel32.QueryFullProcessImageNameW.argtypes = [
        wt.HANDLE,
        wt.DWORD,
        wt.LPWSTR,
        ctypes.POINTER(wt.DWORD),
    ]
    kernel32.QueryFullProcessImageNameW.restype = wt.BOOL
    kernel32.GetProcessTimes.argtypes = [
        wt.HANDLE,
        ctypes.POINTER(wt.FILETIME),
        ctypes.POINTER(wt.FILETIME),
        ctypes.POINTER(wt.FILETIME),
        ctypes.POINTER(wt.FILETIME),
    ]
    kernel32.GetProcessTimes.restype = wt.BOOL
    kernel32.CreateToolhelp32Snapshot.argtypes = [wt.DWORD, wt.DWORD]
    kernel32.CreateToolhelp32Snapshot.restype = wt.HANDLE
    kernel32.Process32FirstW.argtypes = [wt.HANDLE, ctypes.POINTER(PROCESSENTRY32W)]
    kernel32.Process32FirstW.restype = wt.BOOL
    kernel32.Process32NextW.argtypes = [wt.HANDLE, ctypes.POINTER(PROCESSENTRY32W)]
    kernel32.Process32NextW.restype = wt.BOOL
    kernel32.ProcessIdToSessionId.argtypes = [wt.DWORD, ctypes.POINTER(wt.DWORD)]
    kernel32.ProcessIdToSessionId.restype = wt.BOOL
    kernel32.GetNativeSystemInfo.argtypes = [ctypes.POINTER(SYSTEM_INFO)]
    kernel32.IsWow64Process2.argtypes = [wt.HANDLE, ctypes.POINTER(wt.WORD), ctypes.POINTER(wt.WORD)]
    kernel32.IsWow64Process2.restype = wt.BOOL
    kernel32.GetCurrentProcess.restype = wt.HANDLE
    kernel32.GetCurrentProcessId.restype = wt.DWORD
    kernel32.DuplicateHandle.argtypes = [
        wt.HANDLE,
        wt.HANDLE,
        wt.HANDLE,
        ctypes.POINTER(wt.HANDLE),
        wt.DWORD,
        wt.BOOL,
        wt.DWORD,
    ]
    kernel32.DuplicateHandle.restype = wt.BOOL
    kernel32.SetFilePointerEx.argtypes = [
        wt.HANDLE,
        ctypes.c_longlong,
        ctypes.POINTER(ctypes.c_longlong),
        wt.DWORD,
    ]
    kernel32.SetFilePointerEx.restype = wt.BOOL

    version_dll.GetFileVersionInfoSizeW.argtypes = [wt.LPCWSTR, ctypes.POINTER(wt.DWORD)]
    version_dll.GetFileVersionInfoSizeW.restype = wt.DWORD
    version_dll.GetFileVersionInfoW.argtypes = [wt.LPCWSTR, wt.DWORD, wt.DWORD, wt.LPVOID]
    version_dll.GetFileVersionInfoW.restype = wt.BOOL
    version_dll.VerQueryValueW.argtypes = [
        wt.LPCVOID,
        wt.LPCWSTR,
        ctypes.POINTER(wt.LPVOID),
        ctypes.POINTER(wt.UINT),
    ]
    version_dll.VerQueryValueW.restype = wt.BOOL
    ntdll.RtlGetVersion.argtypes = [ctypes.POINTER(RTL_OSVERSIONINFOEXW)]
    ntdll.RtlGetVersion.restype = wt.LONG
    ntdll.NtQueryInformationProcess.argtypes = [
        wt.HANDLE,
        wt.DWORD,
        wt.LPVOID,
        wt.ULONG,
        ctypes.POINTER(wt.ULONG),
    ]
    ntdll.NtQueryInformationProcess.restype = wt.LONG

    advapi32.OpenSCManagerW.argtypes = [wt.LPCWSTR, wt.LPCWSTR, wt.DWORD]
    advapi32.OpenSCManagerW.restype = wt.HANDLE
    advapi32.OpenServiceW.argtypes = [wt.HANDLE, wt.LPCWSTR, wt.DWORD]
    advapi32.OpenServiceW.restype = wt.HANDLE
    advapi32.QueryServiceStatusEx.argtypes = [
        wt.HANDLE,
        ctypes.c_int,
        LPBYTE,
        wt.DWORD,
        ctypes.POINTER(wt.DWORD),
    ]
    advapi32.QueryServiceStatusEx.restype = wt.BOOL
    advapi32.QueryServiceConfigW.argtypes = [
        wt.HANDLE,
        ctypes.POINTER(QUERY_SERVICE_CONFIGW),
        wt.DWORD,
        ctypes.POINTER(wt.DWORD),
    ]
    advapi32.QueryServiceConfigW.restype = wt.BOOL
    advapi32.CloseServiceHandle.argtypes = [wt.HANDLE]
    advapi32.CloseServiceHandle.restype = wt.BOOL

    wintrust.WinVerifyTrust.argtypes = [wt.HWND, ctypes.POINTER(GUID), ctypes.POINTER(WINTRUST_DATA)]
    wintrust.WinVerifyTrust.restype = wt.LONG
    wintrust.WTHelperProvDataFromStateData.argtypes = [wt.HANDLE]
    wintrust.WTHelperProvDataFromStateData.restype = wt.LPVOID
    wintrust.WTHelperGetProvSignerFromChain.argtypes = [wt.LPVOID, wt.DWORD, wt.BOOL, wt.DWORD]
    wintrust.WTHelperGetProvSignerFromChain.restype = ctypes.POINTER(CRYPT_PROVIDER_SGNR)
    crypt32.CertGetNameStringW.argtypes = [
        ctypes.POINTER(CERT_CONTEXT),
        wt.DWORD,
        wt.DWORD,
        wt.LPVOID,
        wt.LPWSTR,
        wt.DWORD,
    ]
    crypt32.CertGetNameStringW.restype = wt.DWORD
    crypt32.CertGetEnhancedKeyUsage.argtypes = [
        ctypes.POINTER(CERT_CONTEXT),
        wt.DWORD,
        ctypes.POINTER(CERT_ENHKEY_USAGE),
        ctypes.POINTER(wt.DWORD),
    ]
    crypt32.CertGetEnhancedKeyUsage.restype = wt.BOOL
    psapi.GetProcessMemoryInfo.argtypes = [
        wt.HANDLE,
        ctypes.POINTER(PROCESS_MEMORY_COUNTERS_EX),
        wt.DWORD,
    ]
    psapi.GetProcessMemoryInfo.restype = wt.BOOL


_configure_apis()


def _win_error(operation: str, code: int | None = None) -> StageCError:
    value = ctypes.get_last_error() if code is None else code
    return StageCError(f"{operation} failed with Win32 error {value}: {ctypes.FormatError(value)}")


def _handle_int(handle: wt.HANDLE | int | None) -> int:
    if handle is None:
        return 0
    value = handle if isinstance(handle, int) else handle.value
    return 0 if value is None else int(value)


def _close_handle(handle: wt.HANDLE | int | None) -> bool:
    value = _handle_int(handle)
    if value in (0, INVALID_HANDLE_VALUE):
        return False
    if not kernel32.CloseHandle(wt.HANDLE(value)):
        raise _win_error("CloseHandle")
    return True


def _handle_inheritable(handle: wt.HANDLE | int) -> bool:
    flags = wt.DWORD()
    if not kernel32.GetHandleInformation(wt.HANDLE(_handle_int(handle)), ctypes.byref(flags)):
        raise _win_error("GetHandleInformation")
    return bool(flags.value & HANDLE_FLAG_INHERIT)


def _set_handle_inheritable(handle: wt.HANDLE | int, enabled: bool) -> None:
    value = HANDLE_FLAG_INHERIT if enabled else 0
    if not kernel32.SetHandleInformation(
        wt.HANDLE(_handle_int(handle)), HANDLE_FLAG_INHERIT, value
    ):
        raise _win_error("SetHandleInformation")
    if _handle_inheritable(handle) != enabled:
        raise StageCError("handle inheritance read-back mismatch")


def _filetime_int(value: wt.FILETIME) -> int:
    return (int(value.dwHighDateTime) << 32) | int(value.dwLowDateTime)


def _filetime_iso(value: wt.FILETIME) -> str:
    ticks = _filetime_int(value)
    unix_100ns = ticks - 116444736000000000
    seconds, remainder = divmod(unix_100ns, 10_000_000)
    result = datetime.fromtimestamp(seconds, timezone.utc).replace(
        microsecond=remainder // 10
    )
    return result.isoformat(timespec="microseconds").replace("+00:00", "Z")


def _receipt_ref(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": str(record["path"]),
        "bytes": int(record["bytes"]),
        "sha256": str(record["sha256"]).upper(),
    }


def _resource_snapshot() -> dict[str, Any]:
    counters = PROCESS_MEMORY_COUNTERS_EX()
    counters.cb = ctypes.sizeof(counters)
    if not psapi.GetProcessMemoryInfo(
        kernel32.GetCurrentProcess(), ctypes.byref(counters), ctypes.sizeof(counters)
    ):
        raise _win_error("GetProcessMemoryInfo")
    result = {
        "working_set_bytes": int(counters.WorkingSetSize),
        "peak_working_set_bytes": int(counters.PeakWorkingSetSize),
        "private_bytes": int(counters.PrivateUsage),
        "peak_pagefile_bytes": int(counters.PeakPagefileUsage),
        "limit_bytes": MAX_COMBINED_RESIDENT_BYTES,
    }
    if (
        result["working_set_bytes"] >= MAX_COMBINED_RESIDENT_BYTES
        or result["peak_working_set_bytes"] >= MAX_COMBINED_RESIDENT_BYTES
    ):
        raise StageCError(f"Stage-C memory envelope exceeded: {result!r}")
    return result


def _process_memory(handle: wt.HANDLE) -> dict[str, int]:
    counters = PROCESS_MEMORY_COUNTERS_EX()
    counters.cb = ctypes.sizeof(counters)
    if not psapi.GetProcessMemoryInfo(handle, ctypes.byref(counters), ctypes.sizeof(counters)):
        raise _win_error("GetProcessMemoryInfo(process)")
    return {
        "working_set_bytes": int(counters.WorkingSetSize),
        "peak_working_set_bytes": int(counters.PeakWorkingSetSize),
        "private_bytes": int(counters.PrivateUsage),
        "peak_pagefile_bytes": int(counters.PeakPagefileUsage),
    }


def _combined_resource_snapshot(
    job: wt.HANDLE, process_handle: wt.HANDLE
) -> dict[str, Any]:
    executor = _process_memory(kernel32.GetCurrentProcess())
    child = _process_memory(process_handle)
    job_state = _job_limits(job)
    current = executor["working_set_bytes"] + child["working_set_bytes"]
    conservative_peak = executor["peak_working_set_bytes"] + max(
        child["peak_working_set_bytes"], job_state["peak_job_memory"]
    )
    result: dict[str, Any] = {
        "executor": executor,
        "child": child,
        "job_peak_process_memory_bytes": job_state["peak_process_memory"],
        "job_peak_memory_bytes": job_state["peak_job_memory"],
        "combined_working_set_bytes": current,
        "combined_conservative_peak_bytes": conservative_peak,
        "limit_bytes": MAX_COMBINED_RESIDENT_BYTES,
    }
    if current >= MAX_COMBINED_RESIDENT_BYTES or conservative_peak >= MAX_COMBINED_RESIDENT_BYTES:
        raise StageCError(f"combined executor+Job memory envelope exceeded: {result!r}")
    return result


def _deadline_guard(
    campaign_started_ns: int,
    operation_started_ns: int | None = None,
    operation_limit_seconds: int | None = None,
) -> dict[str, Any]:
    now_ns = time.monotonic_ns()
    campaign_ms = (now_ns - campaign_started_ns) // 1_000_000
    if campaign_ms >= DEADLINE_SECONDS * 1000:
        raise StageCError("Stage-C absolute deadline exceeded")
    result = {
        "campaign_elapsed_milliseconds": campaign_ms,
        "campaign_limit_milliseconds": DEADLINE_SECONDS * 1000,
    }
    if operation_started_ns is not None and operation_limit_seconds is not None:
        operation_ms = (now_ns - operation_started_ns) // 1_000_000
        result.update(
            {
                "operation_elapsed_milliseconds": operation_ms,
                "operation_limit_milliseconds": operation_limit_seconds * 1000,
            }
        )
        if operation_ms >= operation_limit_seconds * 1000:
            raise StageCError("logical-check hard duration contract exceeded")
    return result


class _HardDeadline:
    """Interrupt a blocked native call without adding a child process or shell."""

    def __init__(self, seconds: float, exit_code: int, label: str) -> None:
        if seconds <= 0:
            raise StageCError(f"invalid {label} hard deadline: {seconds!r}")
        self._seconds = float(seconds)
        self._exit_code = int(exit_code)
        self._label = label
        self._cancel = threading.Event()
        self._thread = threading.Thread(
            target=self._watch,
            name=f"StageC-{label}-deadline",
            daemon=True,
        )
        self._started = False

    def _watch(self) -> None:
        if self._cancel.wait(self._seconds):
            return
        # A hard native-call deadline cannot rely on Python exception delivery.
        # TerminateProcess is deliberately confined to this executor process.
        kernel32.TerminateProcess(kernel32.GetCurrentProcess(), self._exit_code)

    def __enter__(self) -> "_HardDeadline":
        self._thread.start()
        self._started = True
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        self._cancel.set()
        if self._started:
            self._thread.join(timeout=1.0)
        if self._thread.is_alive():
            raise StageCError(f"{self._label} hard-deadline watchdog did not stop")


def _file_id_info_from_handle(handle: wt.HANDLE, path: str) -> dict[str, Any]:
    info = FILE_ID_INFO()
    if not kernel32.GetFileInformationByHandleEx(
        handle,
        18,  # FileIdInfo
        ctypes.byref(info),
        ctypes.sizeof(info),
    ):
        raise _win_error(f"GetFileInformationByHandleEx(FileIdInfo: {path})")
    identifier = bytes(info.FileId.Identifier)
    if len(identifier) != 16:
        raise StageCError(f"FILE_ID_INFO did not return 128 bits: {path}")
    return {
        "volume_serial_64": int(info.VolumeSerialNumber),
        "file_id_128": identifier.hex().upper(),
    }


def _identity_from_handle(
    handle: wt.HANDLE, path: str, include_hash: bool
) -> dict[str, Any]:
    info = BY_HANDLE_FILE_INFORMATION()
    if not kernel32.GetFileInformationByHandle(handle, ctypes.byref(info)):
        raise _win_error(f"GetFileInformationByHandle({path})")
    size = (int(info.nFileSizeHigh) << 32) | int(info.nFileSizeLow)
    file_id_info = _file_id_info_from_handle(handle, path)
    result: dict[str, Any] = {
        "path": os.path.abspath(path),
        "exists": True,
        "attributes": int(info.dwFileAttributes),
        "directory": bool(info.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY),
        "reparse": bool(info.dwFileAttributes & FILE_ATTRIBUTE_REPARSE_POINT),
        "volume_serial": int(info.dwVolumeSerialNumber),
        "file_index": (int(info.nFileIndexHigh) << 32) | int(info.nFileIndexLow),
        **file_id_info,
        "bytes": size,
        "links": int(info.nNumberOfLinks),
        "creation_filetime": _filetime_int(info.ftCreationTime),
        "write_filetime": _filetime_int(info.ftLastWriteTime),
    }
    if include_hash:
        reset_position = ctypes.c_longlong()
        if not kernel32.SetFilePointerEx(
            handle,
            0,
            ctypes.byref(reset_position),
            FILE_BEGIN,
        ):
            raise _win_error(f"SetFilePointerEx(reset before hash: {path})")
        if reset_position.value != 0:
            raise StageCError(f"file hash reset did not reach offset zero: {path}")
        current_process = kernel32.GetCurrentProcess()
        duplicate = wt.HANDLE()
        if not kernel32.DuplicateHandle(
            current_process,
            handle,
            current_process,
            ctypes.byref(duplicate),
            0,
            False,
            DUPLICATE_SAME_ACCESS,
        ):
            raise _win_error("DuplicateHandle(file identity)")
        descriptor = msvcrt.open_osfhandle(_handle_int(duplicate), os.O_RDONLY | os.O_BINARY)
        digest = hashlib.sha256()
        hashed_bytes = 0
        try:
            while True:
                block = os.read(descriptor, 1024 * 1024)
                if not block:
                    break
                hashed_bytes += len(block)
                digest.update(block)
        finally:
            os.close(descriptor)
        if hashed_bytes != size:
            raise StageCError(
                f"held file size/hash mismatch for {path}: {hashed_bytes} != {size}"
            )
        result["sha256"] = digest.hexdigest().upper()
    return result


def _open_held_direct_file(path: str) -> wt.HANDLE:
    state = _require_direct_file(path)
    handle = kernel32.CreateFileW(
        path,
        GENERIC_READ | FILE_READ_ATTRIBUTES,
        FILE_SHARE_READ,
        None,
        OPEN_EXISTING,
        FILE_FLAG_OPEN_REPARSE_POINT,
        None,
    )
    if _handle_int(handle) == INVALID_HANDLE_VALUE:
        raise _win_error(f"CreateFileW-held({path})")
    held = _identity_from_handle(handle, path, include_hash=False)
    if held["reparse"] or held["directory"]:
        _close_handle(handle)
        raise StageCError(f"held path is not a direct file: {path}")
    if (
        held["volume_serial_64"] != state["volume_serial_64"]
        or held["file_id_128"] != state["file_id_128"]
    ):
        _close_handle(handle)
        raise StageCError(f"held file differs from path identity: {path}")
    return handle


def _path_state(path: str, include_hash: bool = False) -> dict[str, Any]:
    direct = os.path.abspath(path)
    attributes = kernel32.GetFileAttributesW(direct)
    if attributes == INVALID_FILE_ATTRIBUTES:
        error = ctypes.get_last_error()
        if error in (ERROR_FILE_NOT_FOUND, ERROR_PATH_NOT_FOUND):
            return {"path": direct, "exists": False, "win32_error": error}
        raise _win_error(f"GetFileAttributesW({direct})", error)
    is_dir = bool(attributes & FILE_ATTRIBUTE_DIRECTORY)
    flags = FILE_FLAG_OPEN_REPARSE_POINT
    if is_dir:
        flags |= FILE_FLAG_BACKUP_SEMANTICS
    handle = kernel32.CreateFileW(
        direct,
        FILE_READ_ATTRIBUTES,
        FILE_SHARE_READ | FILE_SHARE_WRITE | FILE_SHARE_DELETE,
        None,
        OPEN_EXISTING,
        flags,
        None,
    )
    if _handle_int(handle) == INVALID_HANDLE_VALUE:
        raise _win_error(f"CreateFileW({direct})")
    try:
        info = BY_HANDLE_FILE_INFORMATION()
        if not kernel32.GetFileInformationByHandle(handle, ctypes.byref(info)):
            raise _win_error(f"GetFileInformationByHandle({direct})")
        size = (int(info.nFileSizeHigh) << 32) | int(info.nFileSizeLow)
        file_index = (int(info.nFileIndexHigh) << 32) | int(info.nFileIndexLow)
        file_id_info = _file_id_info_from_handle(handle, direct)
        result: dict[str, Any] = {
            "path": direct,
            "exists": True,
            "attributes": int(attributes),
            "directory": is_dir,
            "reparse": bool(attributes & FILE_ATTRIBUTE_REPARSE_POINT),
            "volume_serial": int(info.dwVolumeSerialNumber),
            "file_index": file_index,
            **file_id_info,
            "bytes": size,
            "links": int(info.nNumberOfLinks),
            "creation_filetime": _filetime_int(info.ftCreationTime),
            "write_filetime": _filetime_int(info.ftLastWriteTime),
        }
    finally:
        _close_handle(handle)
    if include_hash and not is_dir:
        bytes_count, digest = _sha256_file(direct)
        if bytes_count != result["bytes"]:
            raise StageCError(f"file size changed while hashing: {direct}")
        result["sha256"] = digest
    return result


def _ancestor_states(path: str) -> list[dict[str, Any]]:
    absolute = os.path.abspath(path)
    drive, tail = os.path.splitdrive(absolute)
    current = drive + os.sep
    result: list[dict[str, Any]] = []
    components = [item for item in tail.split(os.sep) if item]
    for index, component in enumerate(components):
        current = os.path.join(current, component)
        state = _path_state(current)
        state["component_ordinal"] = index
        result.append(state)
        if not state["exists"]:
            break
        if state["reparse"]:
            raise StageCError(f"reparse-point ancestor is forbidden: {current}")
        if index < len(components) - 1 and not state["directory"]:
            raise StageCError(f"non-directory ancestor is forbidden: {current}")
    return result


def _require_direct_file(path: str) -> dict[str, Any]:
    states = _ancestor_states(path)
    state = states[-1]
    if not state["exists"] or state["directory"] or state["reparse"]:
        raise StageCError(f"required direct file is invalid: {path}")
    return state


def _require_direct_directory(path: str) -> dict[str, Any]:
    states = _ancestor_states(path)
    state = states[-1]
    if not state["exists"] or not state["directory"] or state["reparse"]:
        raise StageCError(f"required direct directory is invalid: {path}")
    return state


def _require_absent_leaf(path: str) -> dict[str, Any]:
    states = _ancestor_states(path)
    final = _path_state(path)
    if final["exists"]:
        raise StageCError(f"registered path must be absent: {path}")
    parent = os.path.dirname(path)
    if os.path.exists(parent):
        names = os.listdir(parent)
        leaf = os.path.basename(path)
        collisions = [name for name in names if name.casefold() == leaf.casefold()]
        if collisions:
            raise StageCError(f"case-colliding path exists for {path}: {collisions!r}")
    return {"path": path, "state": final, "ancestors": states}


def _file_version(path: str) -> dict[str, Any]:
    ignored = wt.DWORD()
    size = version_dll.GetFileVersionInfoSizeW(path, ctypes.byref(ignored))
    if not size:
        raise _win_error(f"GetFileVersionInfoSizeW({path})")
    buffer = ctypes.create_string_buffer(size)
    if not version_dll.GetFileVersionInfoW(path, 0, size, buffer):
        raise _win_error(f"GetFileVersionInfoW({path})")
    pointer = wt.LPVOID()
    length = wt.UINT()
    if not version_dll.VerQueryValueW(buffer, "\\", ctypes.byref(pointer), ctypes.byref(length)):
        raise _win_error(f"VerQueryValueW({path})")
    if length.value < ctypes.sizeof(VS_FIXEDFILEINFO):
        raise StageCError(f"short VS_FIXEDFILEINFO for {path}")
    info = ctypes.cast(pointer, ctypes.POINTER(VS_FIXEDFILEINFO)).contents
    if info.dwSignature != 0xFEEF04BD:
        raise StageCError(f"invalid VS_FIXEDFILEINFO signature for {path}")

    def quad(ms: int, ls: int) -> str:
        return f"{ms >> 16}.{ms & 0xFFFF}.{ls >> 16}.{ls & 0xFFFF}"

    return {
        "file_version": quad(info.dwFileVersionMS, info.dwFileVersionLS),
        "product_version": quad(info.dwProductVersionMS, info.dwProductVersionLS),
        "file_flags": int(info.dwFileFlags),
        "file_os": int(info.dwFileOS),
        "file_type": int(info.dwFileType),
    }


def _os_identity() -> dict[str, Any]:
    version = RTL_OSVERSIONINFOEXW()
    version.dwOSVersionInfoSize = ctypes.sizeof(version)
    status = ntdll.RtlGetVersion(ctypes.byref(version))
    if status != 0:
        raise StageCError(f"RtlGetVersion failed with NTSTATUS {status}")
    system = SYSTEM_INFO()
    kernel32.GetNativeSystemInfo(ctypes.byref(system))
    process_machine = wt.WORD()
    native_machine = wt.WORD()
    if not kernel32.IsWow64Process2(
        kernel32.GetCurrentProcess(),
        ctypes.byref(process_machine),
        ctypes.byref(native_machine),
    ):
        raise _win_error("IsWow64Process2")
    kernel_state = _path_state(KERNEL_PATH, include_hash=True)
    if kernel_state["reparse"] or kernel_state["directory"]:
        raise StageCError("kernel image path is not a direct file")
    return {
        "rtl_version": {
            "major": int(version.dwMajorVersion),
            "minor": int(version.dwMinorVersion),
            "build": int(version.dwBuildNumber),
            "platform": int(version.dwPlatformId),
            "service_pack_major": int(version.wServicePackMajor),
            "service_pack_minor": int(version.wServicePackMinor),
            "product_type": int(version.wProductType),
        },
        "native_system": {
            "architecture": int(system.u.arch.wProcessorArchitecture),
            "page_size": int(system.dwPageSize),
            "allocation_granularity": int(system.dwAllocationGranularity),
            "processors": int(system.dwNumberOfProcessors),
            "processor_type": int(system.dwProcessorType),
            "processor_level": int(system.wProcessorLevel),
            "processor_revision": int(system.wProcessorRevision),
        },
        "wow64": {
            "process_machine": int(process_machine.value),
            "native_machine": int(native_machine.value),
            "pointer_bits": ctypes.sizeof(ctypes.c_void_p) * 8,
        },
        "kernel": {"file": kernel_state, "version": _file_version(KERNEL_PATH)},
    }


def _process_image(pid: int) -> tuple[str | None, int | None, int | None]:
    handle = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
    if not handle:
        return None, ctypes.get_last_error(), None
    try:
        capacity = wt.DWORD(32768)
        buffer = ctypes.create_unicode_buffer(capacity.value)
        if not kernel32.QueryFullProcessImageNameW(handle, 0, buffer, ctypes.byref(capacity)):
            return None, ctypes.get_last_error(), None
        created = wt.FILETIME()
        exited = wt.FILETIME()
        kernel = wt.FILETIME()
        user = wt.FILETIME()
        start = None
        if kernel32.GetProcessTimes(
            handle,
            ctypes.byref(created),
            ctypes.byref(exited),
            ctypes.byref(kernel),
            ctypes.byref(user),
        ):
            start = _filetime_int(created)
        return buffer.value, None, start
    finally:
        _close_handle(handle)


def _process_snapshot() -> list[dict[str, Any]]:
    relevant = {
        "wsl.exe",
        "wslservice.exe",
        "wslhost.exe",
        "wslrelay.exe",
        "vmmem.exe",
        "vmmemwsl.exe",
        os.path.basename(sys.executable).casefold(),
    }
    snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
    if _handle_int(snapshot) == INVALID_HANDLE_VALUE:
        raise _win_error("CreateToolhelp32Snapshot")
    rows: list[dict[str, Any]] = []
    try:
        entry = PROCESSENTRY32W()
        entry.dwSize = ctypes.sizeof(entry)
        ok = kernel32.Process32FirstW(snapshot, ctypes.byref(entry))
        while ok:
            name = entry.szExeFile
            pid = int(entry.th32ProcessID)
            if name.casefold() in relevant or pid == os.getpid():
                session = wt.DWORD()
                session_error = None
                if not kernel32.ProcessIdToSessionId(pid, ctypes.byref(session)):
                    session_error = ctypes.get_last_error()
                image, image_error, start = _process_image(pid)
                rows.append(
                    {
                        "pid": pid,
                        "parent_pid": int(entry.th32ParentProcessID),
                        "threads": int(entry.cntThreads),
                        "name": name,
                        "session_id": None if session_error is not None else int(session.value),
                        "session_error": session_error,
                        "image": image,
                        "image_error": image_error,
                        "start_filetime": start,
                    }
                )
            entry.dwSize = ctypes.sizeof(entry)
            ok = kernel32.Process32NextW(snapshot, ctypes.byref(entry))
    finally:
        _close_handle(snapshot)
    return sorted(rows, key=lambda row: (str(row["name"]).casefold(), int(row["pid"])))


def _service_snapshot() -> list[dict[str, Any]]:
    SC_MANAGER_CONNECT = 0x0001
    SERVICE_QUERY_CONFIG = 0x0001
    SERVICE_QUERY_STATUS = 0x0004
    SC_STATUS_PROCESS_INFO = 0
    manager = advapi32.OpenSCManagerW(None, None, SC_MANAGER_CONNECT)
    if not manager:
        raise _win_error("OpenSCManagerW")
    rows: list[dict[str, Any]] = []
    try:
        for name in ("WslService", "LxssManager"):
            service = advapi32.OpenServiceW(
                manager, name, SERVICE_QUERY_CONFIG | SERVICE_QUERY_STATUS
            )
            if not service:
                error = ctypes.get_last_error()
                if error == ERROR_SERVICE_DOES_NOT_EXIST:
                    rows.append({"name": name, "exists": False, "win32_error": error})
                    continue
                raise _win_error(f"OpenServiceW({name})", error)
            try:
                status = SERVICE_STATUS_PROCESS()
                required = wt.DWORD()
                if not advapi32.QueryServiceStatusEx(
                    service,
                    SC_STATUS_PROCESS_INFO,
                    ctypes.cast(ctypes.byref(status), LPBYTE),
                    ctypes.sizeof(status),
                    ctypes.byref(required),
                ):
                    raise _win_error(f"QueryServiceStatusEx({name})")
                needed = wt.DWORD()
                advapi32.QueryServiceConfigW(service, None, 0, ctypes.byref(needed))
                error = ctypes.get_last_error()
                if error != ERROR_INSUFFICIENT_BUFFER or needed.value == 0:
                    raise _win_error(f"QueryServiceConfigW-size({name})", error)
                storage = ctypes.create_string_buffer(needed.value)
                config = ctypes.cast(storage, ctypes.POINTER(QUERY_SERVICE_CONFIGW))
                if not advapi32.QueryServiceConfigW(
                    service, config, needed.value, ctypes.byref(needed)
                ):
                    raise _win_error(f"QueryServiceConfigW({name})")
                item = config.contents
                rows.append(
                    {
                        "name": name,
                        "exists": True,
                        "service_type": int(status.dwServiceType),
                        "state": int(status.dwCurrentState),
                        "controls_accepted": int(status.dwControlsAccepted),
                        "win32_exit_code": int(status.dwWin32ExitCode),
                        "service_exit_code": int(status.dwServiceSpecificExitCode),
                        "checkpoint": int(status.dwCheckPoint),
                        "wait_hint": int(status.dwWaitHint),
                        "pid": int(status.dwProcessId),
                        "service_flags": int(status.dwServiceFlags),
                        "start_type": int(item.dwStartType),
                        "binary_path": item.lpBinaryPathName,
                        "service_account": item.lpServiceStartName,
                    }
                )
            finally:
                if not advapi32.CloseServiceHandle(service):
                    raise _win_error(f"CloseServiceHandle({name})")
    finally:
        if not advapi32.CloseServiceHandle(manager):
            raise _win_error("CloseServiceHandle(SCM)")
    return rows


def _cert_name(context: ctypes.POINTER(CERT_CONTEXT), oid: str, issuer: bool = False) -> str:
    CERT_NAME_ATTR_TYPE = 3
    CERT_NAME_ISSUER_FLAG = 1
    oid_buffer = ctypes.c_char_p(oid.encode("ascii"))
    flags = CERT_NAME_ISSUER_FLAG if issuer else 0
    length = crypt32.CertGetNameStringW(
        context,
        CERT_NAME_ATTR_TYPE,
        flags,
        ctypes.cast(oid_buffer, wt.LPVOID),
        None,
        0,
    )
    if length <= 1:
        return ""
    buffer = ctypes.create_unicode_buffer(length)
    if crypt32.CertGetNameStringW(
        context,
        CERT_NAME_ATTR_TYPE,
        flags,
        ctypes.cast(oid_buffer, wt.LPVOID),
        buffer,
        length,
    ) != length:
        raise StageCError("CertGetNameStringW length changed")
    return buffer.value


def _cert_ekus(context: ctypes.POINTER(CERT_CONTEXT)) -> list[str]:
    size = wt.DWORD()
    if not crypt32.CertGetEnhancedKeyUsage(context, 0, None, ctypes.byref(size)):
        raise _win_error("CertGetEnhancedKeyUsage-size")
    storage = ctypes.create_string_buffer(size.value)
    usage = ctypes.cast(storage, ctypes.POINTER(CERT_ENHKEY_USAGE))
    if not crypt32.CertGetEnhancedKeyUsage(context, 0, usage, ctypes.byref(size)):
        raise _win_error("CertGetEnhancedKeyUsage")
    return sorted(
        usage.contents.rgpszUsageIdentifier[index].decode("ascii")
        for index in range(int(usage.contents.cUsageIdentifier))
    )


def _cert_record(provider: CRYPT_PROVIDER_CERT) -> dict[str, Any]:
    if not provider.pCert or not provider.pCert.contents.pCertInfo:
        raise StageCError("trust provider returned a null certificate")
    context = provider.pCert
    cert = context.contents
    info = cert.pCertInfo.contents
    der = ctypes.string_at(cert.pbCertEncoded, cert.cbCertEncoded)
    serial_raw = ctypes.string_at(info.SerialNumber.pbData, info.SerialNumber.cbData)
    critical = []
    for index in range(int(info.cExtension)):
        extension = info.rgExtension[index]
        if extension.fCritical:
            critical.append(extension.pszObjId.decode("ascii"))
    return {
        "der_bytes": len(der),
        "der_sha256": _sha256_bytes(der),
        "serial": serial_raw[::-1].hex().upper(),
        "subject_cn": _cert_name(context, "2.5.4.3"),
        "subject_o": _cert_name(context, "2.5.4.10"),
        "issuer_cn": _cert_name(context, "2.5.4.3", issuer=True),
        "issuer_o": _cert_name(context, "2.5.4.10", issuer=True),
        "not_before": _filetime_iso(info.NotBefore),
        "not_after": _filetime_iso(info.NotAfter),
        "ekus": _cert_ekus(context),
        "critical_extensions": sorted(critical),
        "trusted_root": bool(provider.fTrustedRoot),
        "self_signed": bool(provider.fSelfSigned),
        "test_cert": bool(provider.fTestCert),
        "revoked_reason": int(provider.dwRevokedReason),
        "confidence": int(provider.dwConfidence),
        "provider_error": int(provider.dwError),
        "ctl_error": int(provider.dwCtlError),
        "cyclic": bool(provider.fIsCyclic),
    }


def _authenticode_identity_v4(
    path: str,
    held_handle: wt.HANDLE,
    held_identity: dict[str, Any],
) -> dict[str, Any]:
    action = GUID.parse("00AAC56B-CD44-11d0-8CC2-00C04FC295EE")
    file_info = WINTRUST_FILE_INFO()
    file_info.cbStruct = ctypes.sizeof(file_info)
    file_info.pcwszFilePath = path
    file_info.hFile = held_handle
    data = WINTRUST_DATA()
    data.cbStruct = ctypes.sizeof(data)
    data.dwUIChoice = 2
    data.fdwRevocationChecks = 1
    data.dwUnionChoice = 1
    data.pFile = ctypes.pointer(file_info)
    data.dwStateAction = 1
    data.dwProvFlags = 0x00000080 | 0x00001000 | 0x00002000
    verify_status = int(wintrust.WinVerifyTrust(wt.HWND(-1), ctypes.byref(action), ctypes.byref(data)))
    close_status = None
    primary_error: BaseException | None = None
    evidence: dict[str, Any] | None = None
    result: dict[str, Any] = {
        "winverifytrust_status": verify_status,
        "ui_choice": int(data.dwUIChoice),
        "revocation_checks": int(data.fdwRevocationChecks),
        "provider_flags": int(data.dwProvFlags),
        "held_file": held_identity,
    }
    try:
        if verify_status != 0 or not data.hWVTStateData:
            raise StageCError(f"WinVerifyTrust rejected {path} with status {verify_status}")
        provider_data = wintrust.WTHelperProvDataFromStateData(data.hWVTStateData)
        if not provider_data:
            raise StageCError("WTHelperProvDataFromStateData returned NULL")
        signer_pointer = wintrust.WTHelperGetProvSignerFromChain(
            provider_data, 0, False, 0
        )
        if not signer_pointer:
            raise StageCError("WTHelperGetProvSignerFromChain returned NULL")
        signer = signer_pointer.contents
        if signer.dwError != 0 or signer.csCertChain < 2:
            raise StageCError(
                f"invalid signer chain error/count: {signer.dwError}/{signer.csCertChain}"
            )
        chain = [
            _cert_record(signer.pasCertChain[index])
            for index in range(int(signer.csCertChain))
        ]
        trust_errors = None
        trust_info = None
        if signer.pChainContext:
            trust_errors = int(signer.pChainContext.contents.TrustStatus.dwErrorStatus)
            trust_info = int(signer.pChainContext.contents.TrustStatus.dwInfoStatus)
        leaf = chain[0]
        root = chain[-1]
        if trust_errors != 0:
            raise StageCError(f"certificate chain trust error: {trust_errors}")
        if leaf["subject_o"] != "Microsoft Corporation":
            raise StageCError("wsl.exe signer organization is not Microsoft Corporation")
        if leaf["subject_cn"] not in ("Microsoft Windows", "Microsoft Corporation"):
            raise StageCError(f"unexpected Microsoft signer CN: {leaf['subject_cn']!r}")
        if "1.3.6.1.5.5.7.3.3" not in leaf["ekus"]:
            raise StageCError("wsl.exe signer lacks code-signing EKU")
        allowed_critical = {
            "2.5.29.14",
            "2.5.29.15",
            "2.5.29.19",
            "2.5.29.32",
            "2.5.29.35",
            "2.5.29.37",
        }
        disallowed_critical = sorted(set(leaf["critical_extensions"]) - allowed_critical)
        if disallowed_critical:
            raise StageCError(
                f"wsl.exe signer has disallowed critical extensions: {disallowed_critical!r}"
            )
        if leaf["test_cert"] or leaf["provider_error"] or leaf["revoked_reason"]:
            raise StageCError("wsl.exe leaf certificate is test/error/revoked")
        if root["subject_o"] != "Microsoft Corporation":
            raise StageCError("wsl.exe root organization is not Microsoft Corporation")
        if not root["trusted_root"] or not root["self_signed"] or root["test_cert"]:
            raise StageCError("wsl.exe root is not a trusted Microsoft self-signed root")
        now = _utc()
        if not (leaf["not_before"] <= now <= leaf["not_after"]):
            raise StageCError("wsl.exe signer certificate is outside its validity period")
        result.update(
            {
                "signer_error": int(signer.dwError),
                "chain_trust_error": trust_errors,
                "chain_trust_info": trust_info,
                "chain": chain,
                "signature_source": "winverifytrust-file-provider",
                "valid_microsoft_signature": True,
            }
        )
    except BaseException as exc:
        primary_error = exc
        raise
    finally:
        if data.hWVTStateData:
            data.dwStateAction = 2
            close_status = int(
                wintrust.WinVerifyTrust(wt.HWND(-1), ctypes.byref(action), ctypes.byref(data))
            )
        result["state_close_status"] = close_status
        if close_status not in (None, 0):
            close_error = StageCError(
                f"WinVerifyTrust state close failed: {close_status}"
            )
            if primary_error is not None:
                secondary = list(getattr(primary_error, "secondary_errors", []))
                secondary.append(_error_record(close_error))
                setattr(primary_error, "secondary_errors", secondary)
            else:
                close_error.wintrust_attempt = dict(result)
                raise close_error
    return result


_V5_TRUST_E_NOSIGNATURE = 0x800B0100
_V5_CRYPT_E_NOT_FOUND = 0x80092004
_V5_ERROR_NOT_FOUND = 1168
_V5_WTD_CHOICE_FILE = 1
_V5_WTD_CHOICE_CATALOG = 2
_V5_WTD_STATEACTION_VERIFY = 1
_V5_WTD_STATEACTION_CLOSE = 2
_V5_WTD_UI_NONE = 2
_V5_WTD_REVOKE_WHOLECHAIN = 1
_V5_WTD_REVOCATION_CHECK_CHAIN_EXCLUDE_ROOT = 0x80
_V5_WTD_CACHE_ONLY_URL_RETRIEVAL = 0x1000
_V5_WTD_DISABLE_MD2_MD4 = 0x2000
_V5_SHA256_BYTES = 32
_V5_FILE_BEGIN = 0
_V5_FILE_CURRENT = 1
_V5_C01_RECEIPT_CONTEXT: dict[str, Any] | None = None


def _v5_c01_emit(kind: str, payload: Mapping[str, Any]) -> None:
    context = _V5_C01_RECEIPT_CONTEXT
    if context is None:
        raise StageCError("C01 receipt emission requires an active receipt context")
    chain = _ACTIVE_GLOBAL_RECEIPT_CHAIN
    if chain is None or chain.head is None:
        raise StageCError("C01 receipt emission requires a durable global-chain head")
    if _receipt_ref(dict(context["head"])) != _receipt_ref(dict(chain.head)):
        raise StageCError("C01 receipt context does not match the global-chain head")
    if kind in ("catalog_fallback_intent", "catalog_hash"):
        context["pending_raw_events"].append({"kind": kind, **dict(payload)})
        return
    sequence = int(context["sequence"]) + 1
    schemas = {
        "trust_intent": SCHEMA_C01_TRUST_INTENT,
        "embedded_attempt": SCHEMA_C01_EMBEDDED,
        "catalog_enumeration": SCHEMA_C01_ENUMERATION,
        "catalog_candidate_intent": SCHEMA_C01_CANDIDATE_INTENT,
        "catalog_candidate_result": SCHEMA_C01_CANDIDATE_RESULT,
        "trust_success": SCHEMA_C01_RESULT,
        "trust_failure": SCHEMA_C01_FAILURE,
    }
    if kind not in schemas:
        raise StageCError(f"unregistered C01 receipt kind: {kind}")
    declared_outcome = str(payload.get("outcome", ""))
    is_failure = (
        kind == "trust_failure"
        or payload.get("error") is not None
        or declared_outcome == "failure"
        or (
            kind == "catalog_candidate_result"
            and payload.get("accepted") is not True
        )
    )
    receipt_kind = kind
    schema = schemas[kind]
    if is_failure and kind in ("embedded_attempt", "catalog_enumeration"):
        receipt_kind = f"{kind}_failure"
        schema = SCHEMA_C01_FAILURE
    ordinal: int | None = None
    if kind.startswith("catalog_candidate_"):
        ordinal = int(payload["ordinal"])
        identity = payload.get("identity")
        if not isinstance(identity, Mapping):
            raise StageCError("candidate receipt lacks held identity")
        candidate_sha256 = str(identity.get("sha256", "")).lower()
        if not re.fullmatch(r"[0-9a-f]{64}", candidate_sha256):
            raise StageCError("candidate receipt SHA-256 is invalid")
        candidate_dir = os.path.join(
            str(context["directory"]),
            "catalog_candidates",
            f"{ordinal:04d}-{candidate_sha256}",
        )
        if not os.path.isdir(candidate_dir):
            _mkdir_new(candidate_dir)
        if kind == "catalog_candidate_intent":
            leaf = "candidate_intent.json"
        elif is_failure:
            leaf = "candidate_failure.json"
            schema = SCHEMA_C01_CANDIDATE_FAILURE
            receipt_kind = "catalog_candidate_failure"
        else:
            leaf = "candidate_result.json"
        final_path = os.path.join(candidate_dir, leaf)
    else:
        leaves = {
            "trust_intent": "trust_intent.json",
            "embedded_attempt": "embedded_attempt.json",
            "catalog_enumeration": "catalog_enumeration.json",
            "trust_success": "trust_success.json",
            "trust_failure": "trust_failure.json",
        }
        final_path = os.path.join(str(context["directory"]), leaves[kind])
    prior = context["head"]
    prior_identity = context["head_identity"]
    raw_events = list(context["pending_raw_events"])
    authority = {
        name: context["common"][name]
        for name in (
            "packet",
            "identity_ledger",
            "v4_manifest",
            "interpreter",
            "execution_authority",
            "perf_lease_state",
        )
    }
    envelope = {
        "schema": schema,
        "attempt_id": context["common"]["attempt_id"],
        "receipt_id": (
            f"c01:candidate:{ordinal:04d}:{receipt_kind.rsplit('_', 1)[-1]}"
            if ordinal is not None
            else f"c01:{receipt_kind.replace('_', '-')}"
        ),
        "receipt_kind": receipt_kind,
        "phase": "C01",
        "created_utc": _utc(),
        "sequence": sequence,
        "producer": context["common"]["executor"],
        "authority": authority,
        "predecessor": prior_identity,
        "outcome": (
            "failure"
            if is_failure
            else "intent"
            if kind.endswith("intent")
            else "non_success"
            if declared_outcome == "classified_non_success"
            else "success"
        ),
        "payload": {
            **dict(payload),
            "raw_api_events": raw_events,
        },
        "primary_error": payload.get("error"),
        "secondary_errors": [],
    }
    record = _atomic_json(
        final_path,
        envelope,
    )
    try:
        reopened = _v5_receipt_from_final(final_path)
        if _receipt_ref(reopened) != _receipt_ref(record):
            raise StageCError("C01 receipt changed during reopen validation")
        record_ref = {
            **_receipt_ref(record),
            "schema": schema,
            "sequence": sequence,
            "predecessor": prior_identity,
        }
        if context["pending_raw_events"][: len(raw_events)] != raw_events:
            raise StageCError("C01 raw-event buffer changed during receipt promotion")
        context["head"] = record
        context["head_identity"] = record_ref
        context["chain"].append(record_ref)
        context["sequence"] = sequence
        del context["pending_raw_events"][: len(raw_events)]
    except BaseException as exc:
        raise _ReceiptRegistrationLost(
            phase=f"C01:{kind}",
            promoted_receipt=_receipt_ref(record),
            prior_receipt=_receipt_ref(prior),
            cause=exc,
            containment={
                "owner": "C01_no_child",
                "terminal": True,
                "zero_pid": True,
                "containment_errors": [],
            },
            attempted_consumer_id=str(envelope["receipt_id"]),
            attempt_id=str(context["common"]["attempt_id"]),
            durable_head=_receipt_ref(prior),
        ) from exc


def _v5_record_c01_event(
    events: list[dict[str, Any]], kind: str, payload: Mapping[str, Any]
) -> None:
    event = {
        "event_schema": "anysolver.no_numba_residual.stage_c.c01_raw_event/2",
        "event_ordinal": len(events),
        "kind": kind,
        **dict(payload),
    }
    events.append(event)
    _v5_c01_emit(kind, event)


def _v5_status_u32(value: int) -> int:
    return int(value) & 0xFFFFFFFF


def _v5_handle(value: Any) -> wt.HANDLE:
    raw = value.value if hasattr(value, "value") else value
    return wt.HANDLE(raw)


def _v5_catalog_apis() -> tuple[Any, Any]:
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    wintrust = ctypes.WinDLL("wintrust", use_last_error=True)

    kernel32.SetFilePointerEx.argtypes = [
        wt.HANDLE,
        ctypes.c_longlong,
        ctypes.POINTER(ctypes.c_longlong),
        wt.DWORD,
    ]
    kernel32.SetFilePointerEx.restype = wt.BOOL
    kernel32.CloseHandle.argtypes = [wt.HANDLE]
    kernel32.CloseHandle.restype = wt.BOOL

    wintrust.WinVerifyTrust.argtypes = [
        wt.HWND,
        ctypes.POINTER(GUID),
        ctypes.POINTER(WINTRUST_DATA),
    ]
    wintrust.WinVerifyTrust.restype = wt.LONG
    wintrust.WTHelperProvDataFromStateData.argtypes = [wt.HANDLE]
    wintrust.WTHelperProvDataFromStateData.restype = ctypes.POINTER(CRYPT_PROVIDER_DATA)
    wintrust.WTHelperGetProvSignerFromChain.argtypes = [
        ctypes.POINTER(CRYPT_PROVIDER_DATA),
        wt.DWORD,
        wt.BOOL,
        wt.DWORD,
    ]
    wintrust.WTHelperGetProvSignerFromChain.restype = ctypes.POINTER(CRYPT_PROVIDER_SGNR)

    wintrust.CryptCATAdminAcquireContext2.argtypes = [
        ctypes.POINTER(wt.HANDLE),
        ctypes.POINTER(GUID),
        wt.LPCWSTR,
        ctypes.c_void_p,
        wt.DWORD,
    ]
    wintrust.CryptCATAdminAcquireContext2.restype = wt.BOOL
    wintrust.CryptCATAdminCalcHashFromFileHandle2.argtypes = [
        wt.HANDLE,
        wt.HANDLE,
        ctypes.POINTER(wt.DWORD),
        ctypes.POINTER(ctypes.c_ubyte),
        wt.DWORD,
    ]
    wintrust.CryptCATAdminCalcHashFromFileHandle2.restype = wt.BOOL
    wintrust.CryptCATAdminEnumCatalogFromHash.argtypes = [
        wt.HANDLE,
        ctypes.POINTER(ctypes.c_ubyte),
        wt.DWORD,
        wt.DWORD,
        ctypes.POINTER(wt.HANDLE),
    ]
    wintrust.CryptCATAdminEnumCatalogFromHash.restype = wt.HANDLE
    wintrust.CryptCATCatalogInfoFromContext.argtypes = [
        wt.HANDLE,
        ctypes.POINTER(CATALOG_INFO),
        wt.DWORD,
    ]
    wintrust.CryptCATCatalogInfoFromContext.restype = wt.BOOL
    wintrust.CryptCATAdminReleaseCatalogContext.argtypes = [wt.HANDLE, wt.HANDLE, wt.DWORD]
    wintrust.CryptCATAdminReleaseCatalogContext.restype = wt.BOOL
    wintrust.CryptCATAdminReleaseContext.argtypes = [wt.HANDLE, wt.DWORD]
    wintrust.CryptCATAdminReleaseContext.restype = wt.BOOL
    return kernel32, wintrust


def _v5_provider_snapshot(wintrust: Any, data: WINTRUST_DATA) -> dict[str, Any]:
    result: dict[str, Any] = {
        "state_handle_present": bool(data.hWVTStateData),
        "provider_present": False,
        "signer_present": False,
        "signer_count": 0,
        "certificate_count": 0,
        "certificate_errors": [],
    }
    if not data.hWVTStateData:
        return result
    provider = wintrust.WTHelperProvDataFromStateData(data.hWVTStateData)
    if not provider:
        return result
    result["provider_present"] = True
    result["signer_count"] = int(provider.contents.csSigners)
    signer = wintrust.WTHelperGetProvSignerFromChain(provider, 0, False, 0)
    if not signer:
        return result
    result["signer_present"] = True
    result["signer_error"] = _v5_status_u32(int(signer.contents.dwError))
    result["certificate_count"] = int(signer.contents.csCertChain)
    errors: list[dict[str, int]] = []
    for index in range(int(signer.contents.csCertChain)):
        cert = signer.contents.pasCertChain[index]
        errors.append(
            {
                "ordinal": index,
                "error": _v5_status_u32(int(cert.dwError)),
                "confidence": int(cert.dwConfidence),
            }
        )
    result["certificate_errors"] = errors
    result["chain"] = [
        _cert_record(signer.contents.pasCertChain[index])
        for index in range(int(signer.contents.csCertChain))
    ]
    if signer.contents.pChainContext:
        result["chain_trust_error"] = int(
            signer.contents.pChainContext.contents.TrustStatus.dwErrorStatus
        )
        result["chain_trust_info"] = int(
            signer.contents.pChainContext.contents.TrustStatus.dwInfoStatus
        )
    else:
        result["chain_trust_error"] = None
        result["chain_trust_info"] = None
    return result


def _v5_validate_microsoft_provider(provider: Mapping[str, Any]) -> dict[str, Any]:
    if provider.get("provider_present") is not True:
        raise StageCError("WinTrust provider is absent")
    if provider.get("signer_present") is not True:
        raise StageCError("WinTrust provider signer is absent")
    chain = provider.get("chain")
    if not isinstance(chain, list) or len(chain) < 2:
        raise StageCError("WinTrust provider lacks a complete signer chain")
    if int(provider.get("signer_error", 0)) != 0:
        raise StageCError("WinTrust provider signer reports an error")
    if provider.get("chain_trust_error") is None or provider.get("chain_trust_info") is None:
        raise StageCError("WinTrust provider lacks pChainContext trust evidence")
    if provider.get("chain_trust_error") != 0:
        raise StageCError("WinTrust provider chain reports a trust error")
    if any(int(row.get("error", 0)) != 0 for row in provider.get("certificate_errors", [])):
        raise StageCError("WinTrust provider certificate chain reports an error")
    leaf = chain[0]
    root = chain[-1]
    if leaf.get("subject_o") != "Microsoft Corporation":
        raise StageCError("WinTrust leaf organization is not Microsoft Corporation")
    if leaf.get("subject_cn") not in ("Microsoft Windows", "Microsoft Corporation"):
        raise StageCError("WinTrust leaf common name is not accepted")
    if "1.3.6.1.5.5.7.3.3" not in leaf.get("ekus", []):
        raise StageCError("WinTrust leaf lacks code-signing EKU")
    allowed_critical = {
        "2.5.29.14",
        "2.5.29.15",
        "2.5.29.19",
        "2.5.29.32",
        "2.5.29.35",
        "2.5.29.37",
    }
    if set(leaf.get("critical_extensions", [])) - allowed_critical:
        raise StageCError("WinTrust leaf has an unapproved critical extension")
    if leaf.get("test_cert") or leaf.get("provider_error") or leaf.get("revoked_reason"):
        raise StageCError("WinTrust leaf is test/error/revoked")
    if root.get("subject_o") != "Microsoft Corporation":
        raise StageCError("WinTrust root organization is not Microsoft Corporation")
    if not root.get("trusted_root") or not root.get("self_signed") or root.get("test_cert"):
        raise StageCError("WinTrust root is not an accepted Microsoft root")
    now = _utc()
    if not (str(leaf.get("not_before", "")) <= now <= str(leaf.get("not_after", ""))):
        raise StageCError("WinTrust leaf is outside its validity period")
    return {
        "chain": chain,
        "leaf": leaf,
        "root": root,
        "valid_microsoft_signature": True,
    }


def _v5_wintrust_attempt(
    *,
    source: str,
    union_choice: int,
    union_value: Any,
) -> dict[str, Any]:
    _, wintrust = _v5_catalog_apis()
    action = GUID.parse("00AAC56B-CD44-11d0-8CC2-00C04FC295EE")
    data = WINTRUST_DATA()
    data.cbStruct = ctypes.sizeof(data)
    data.dwUIChoice = _V5_WTD_UI_NONE
    data.fdwRevocationChecks = _V5_WTD_REVOKE_WHOLECHAIN
    data.dwUnionChoice = union_choice
    if union_choice == _V5_WTD_CHOICE_FILE:
        data.pFile = ctypes.pointer(union_value)
    elif union_choice == _V5_WTD_CHOICE_CATALOG:
        data.pCatalog = ctypes.pointer(union_value)
    else:
        raise StageCError(f"unsupported WinTrust union choice: {union_choice}")
    data.dwStateAction = _V5_WTD_STATEACTION_VERIFY
    data.dwProvFlags = (
        _V5_WTD_REVOCATION_CHECK_CHAIN_EXCLUDE_ROOT
        | _V5_WTD_CACHE_ONLY_URL_RETRIEVAL
        | _V5_WTD_DISABLE_MD2_MD4
    )

    status = int(wintrust.WinVerifyTrust(None, ctypes.byref(action), ctypes.byref(data)))
    status_u32 = _v5_status_u32(status)
    provider: dict[str, Any]
    provider_error: dict[str, str] | None = None
    try:
        provider = _v5_provider_snapshot(wintrust, data)
    except BaseException as exc:
        provider = {
            "state_handle_present": bool(data.hWVTStateData),
            "provider_present": False,
            "signer_present": False,
            "signer_count": 0,
            "certificate_count": 0,
            "certificate_errors": [],
        }
        provider_error = {
            "type": type(exc).__name__,
            "message_sha256": hashlib.sha256(str(exc).encode("utf-8")).hexdigest(),
        }

    close_status_u32: int | None = None
    close_error: BaseException | None = None
    if data.hWVTStateData:
        data.dwStateAction = _V5_WTD_STATEACTION_CLOSE
        try:
            close_status_u32 = _v5_status_u32(
                int(wintrust.WinVerifyTrust(None, ctypes.byref(action), ctypes.byref(data)))
            )
        except BaseException as exc:
            close_error = exc
    result = {
        "source": source,
        "verify_call": {
            "union_choice": union_choice,
            "state_action": _V5_WTD_STATEACTION_VERIFY,
            "status": status_u32,
            "status_hex": f"0x{status_u32:08X}",
        },
        "status": status_u32,
        "status_hex": f"0x{status_u32:08X}",
        "provider": provider,
        "provider_error": provider_error,
        "state_close_status": close_status_u32,
        "state_close_status_hex": (
            None if close_status_u32 is None else f"0x{close_status_u32:08X}"
        ),
        "state_close_error": (
            None if close_error is None else _error_record(close_error)
        ),
        "state_close_attempted": bool(data.hWVTStateData),
        "state_ownership_cleared": bool(
            data.hWVTStateData and close_error is None and close_status_u32 == 0
        ),
        "close_proof": {
            "attempted": bool(data.hWVTStateData),
            "status": close_status_u32,
            "status_hex": (
                None if close_status_u32 is None else f"0x{close_status_u32:08X}"
            ),
            "error": None if close_error is None else _error_record(close_error),
            "state_ownership_cleared": bool(
                data.hWVTStateData and close_error is None and close_status_u32 == 0
            ),
        },
    }
    if close_error is not None or close_status_u32 not in (None, 0):
        detail = (
            f"exception {type(close_error).__name__}"
            if close_error is not None
            else f"status 0x{close_status_u32:08X}"
        )
        verify_failed = status_u32 != 0
        error = StageCError(
            (
                f"WinVerifyTrust {source} VERIFY failed: 0x{status_u32:08X}; "
                f"state CLOSE also failed: {detail}"
            )
            if verify_failed
            else f"WinVerifyTrust state close failed for {source}: {detail}"
        )
        error.wintrust_attempt = result
        error.wintrust_close_failed = True
        error.secondary_errors = [
            row
            for row in (
                None if provider_error is None else {"provider_extraction": provider_error},
                {
                    "wintrust_close": {
                        "status": close_status_u32,
                        "status_hex": (
                            None
                            if close_status_u32 is None
                            else f"0x{close_status_u32:08X}"
                        ),
                        "error": (
                            None if close_error is None else _error_record(close_error)
                        ),
                    }
                },
            )
            if row is not None
        ]
        raise error from close_error
    if provider_error is not None:
        error = StageCError(
            f"WinTrust {source} provider extraction failed after VERIFY"
        )
        error.wintrust_attempt = result
        error.secondary_errors = [{"provider_extraction": provider_error}]
        raise error
    if status_u32 == 0 and (
        provider.get("provider_present") is not True
        or provider.get("signer_present") is not True
    ):
        error = StageCError(
            f"successful WinVerifyTrust {source} attempt lacked provider/signer evidence"
        )
        error.wintrust_attempt = result
        error.secondary_errors = [
            {
                "provider_or_signer_absent": {
                    "provider_present": provider.get("provider_present"),
                    "signer_present": provider.get("signer_present"),
                }
            }
        ]
        raise error
    return result


def _v5_embedded_attempt(path: str, held_handle: int) -> dict[str, Any]:
    file_info = WINTRUST_FILE_INFO()
    file_info.cbStruct = ctypes.sizeof(file_info)
    file_info.pcwszFilePath = path
    file_info.hFile = _v5_handle(held_handle)
    file_info.pgKnownSubject = None
    return _v5_wintrust_attempt(
        source="embedded",
        union_choice=_V5_WTD_CHOICE_FILE,
        union_value=file_info,
    )


def _v5_catalog_hash(
    admin: wt.HANDLE, held_handle: int
) -> tuple[bytes, dict[str, Any]]:
    kernel32, wintrust = _v5_catalog_apis()
    handle = _v5_handle(held_handle)
    saved = ctypes.c_longlong()
    if not kernel32.SetFilePointerEx(
        handle, ctypes.c_longlong(0), ctypes.byref(saved), _V5_FILE_CURRENT
    ):
        raise StageCError(f"SetFilePointerEx(CURRENT) failed: {ctypes.get_last_error()}")
    primary_error: BaseException | None = None
    evidence: dict[str, Any] = {
        "algorithm": "SHA256",
        "sizing": None,
        "fill": None,
        "file_position_before": int(saved.value),
        "file_position_after_restore": None,
        "file_position_restored": False,
        "member_tag": None,
    }
    try:
        if not kernel32.SetFilePointerEx(
            handle, ctypes.c_longlong(0), None, _V5_FILE_BEGIN
        ):
            raise StageCError(f"SetFilePointerEx(BEGIN) failed: {ctypes.get_last_error()}")
        size = wt.DWORD(0)
        ctypes.set_last_error(0)
        size_ok = bool(
            wintrust.CryptCATAdminCalcHashFromFileHandle2(
                admin, handle, ctypes.byref(size), None, 0
            )
        )
        size_error = _v5_status_u32(ctypes.get_last_error())
        evidence["sizing"] = {
            "returned": size_ok,
            "requested_bytes": 0,
            "final_bytes": int(size.value),
            "flags": 0,
            "last_error": size_error,
        }
        if not size_ok:
            raise StageCError(
                "CryptCATAdminCalcHashFromFileHandle2(size) failed: "
                f"{ctypes.get_last_error()}"
            )
        if int(size.value) != _V5_SHA256_BYTES:
            raise StageCError(
                "catalog member hash sizing was not exact SHA-256: "
                f"expected {_V5_SHA256_BYTES}, got {int(size.value)}"
            )
        buffer = (ctypes.c_ubyte * _V5_SHA256_BYTES)()
        fill_size = wt.DWORD(_V5_SHA256_BYTES)
        ctypes.set_last_error(0)
        fill_ok = bool(
            wintrust.CryptCATAdminCalcHashFromFileHandle2(
                admin, handle, ctypes.byref(fill_size), buffer, 0
            )
        )
        fill_error = _v5_status_u32(ctypes.get_last_error())
        evidence["fill"] = {
            "returned": fill_ok,
            "requested_bytes": _V5_SHA256_BYTES,
            "final_bytes": int(fill_size.value),
            "flags": 0,
            "last_error": fill_error,
            "buffer_hex": bytes(buffer).hex(),
        }
        if not fill_ok:
            raise StageCError(
                "CryptCATAdminCalcHashFromFileHandle2(fill) failed: "
                f"{ctypes.get_last_error()}"
            )
        if int(fill_size.value) != _V5_SHA256_BYTES:
            raise StageCError(
                "catalog member hash fill length changed: "
                f"expected {_V5_SHA256_BYTES}, got {int(fill_size.value)}"
            )
        member_hash = bytes(buffer)
        evidence["fill"]["buffer_hex"] = member_hash.hex()
        evidence["member_tag"] = member_hash.hex().upper()
        return member_hash, evidence
    except BaseException as exc:
        primary_error = exc
        setattr(exc, "catalog_hash_evidence", dict(evidence))
        raise
    finally:
        if not kernel32.SetFilePointerEx(
            handle, ctypes.c_longlong(saved.value), None, _V5_FILE_BEGIN
        ):
            restore_error = StageCError(
                f"SetFilePointerEx(restore) failed: {ctypes.get_last_error()}"
            )
            if primary_error is not None:
                setattr(primary_error, "catalog_hash_restore_error", str(restore_error))
                evidence["restore_error"] = _error_record(restore_error)
            else:
                raise restore_error
        else:
            restored = ctypes.c_longlong()
            if kernel32.SetFilePointerEx(
                handle, ctypes.c_longlong(0), ctypes.byref(restored), _V5_FILE_CURRENT
            ):
                evidence["file_position_after_restore"] = int(restored.value)
                evidence["file_position_restored"] = int(restored.value) == int(saved.value)
                if not evidence["file_position_restored"]:
                    position_error = StageCError(
                        "catalog hash file position did not restore exactly"
                    )
                    if primary_error is not None:
                        setattr(primary_error, "catalog_hash_position_error", str(position_error))
                        evidence["restore_error"] = _error_record(position_error)
                    else:
                        raise position_error
            else:
                position_error = StageCError(
                    f"SetFilePointerEx(post-restore CURRENT) failed: {ctypes.get_last_error()}"
                )
                if primary_error is not None:
                    setattr(primary_error, "catalog_hash_position_error", str(position_error))
                    evidence["restore_error"] = _error_record(position_error)
                else:
                    raise position_error
        if primary_error is not None:
            setattr(primary_error, "catalog_hash_evidence", dict(evidence))


def _v5_release_catalog_context(wintrust: Any, admin: wt.HANDLE, catalog: wt.HANDLE) -> None:
    if catalog and not wintrust.CryptCATAdminReleaseCatalogContext(admin, catalog, 0):
        raise StageCError(
            f"CryptCATAdminReleaseCatalogContext failed: {ctypes.get_last_error()}"
        )


def _v5_catalog_paths(
    admin: wt.HANDLE, member_hash: bytes
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    _, wintrust = _v5_catalog_apis()
    hash_buffer = (ctypes.c_ubyte * len(member_hash)).from_buffer_copy(member_hash)
    previous = wt.HANDLE()
    descriptors: list[dict[str, Any]] = []
    calls: list[dict[str, Any]] = []
    evidence: dict[str, Any] = {
        "hash_bytes": len(member_hash),
        "enumeration_flags": 0,
        "calls": calls,
        "candidate_descriptor_count": 0,
        "clean_end": False,
    }
    primary_error: BaseException | None = None
    try:
        while True:
            ctypes.set_last_error(0)
            previous_arg = ctypes.byref(previous) if previous.value else None
            current = wintrust.CryptCATAdminEnumCatalogFromHash(
                admin,
                hash_buffer,
                len(member_hash),
                0,
                previous_arg,
            )
            # The API consumes a non-null previous HCATINFO on every continuation.
            previous = wt.HANDLE()
            if not current:
                error = _v5_status_u32(ctypes.get_last_error())
                calls.append(
                    {
                        "source_ordinal": len(descriptors),
                        "enum_returned_context": False,
                        "enum_last_error": error,
                        "clean_end": error
                        in (0, _V5_ERROR_NOT_FOUND, _V5_CRYPT_E_NOT_FOUND),
                    }
                )
                if error not in (0, _V5_ERROR_NOT_FOUND, _V5_CRYPT_E_NOT_FOUND):
                    raise StageCError(
                        "CryptCATAdminEnumCatalogFromHash failed before clean end: "
                        f"0x{error:08X}"
                    )
                break
            previous = _v5_handle(current)
            info = CATALOG_INFO()
            info.cbStruct = ctypes.sizeof(info)
            ctypes.set_last_error(0)
            info_ok = bool(
                wintrust.CryptCATCatalogInfoFromContext(
                    previous, ctypes.byref(info), 0
                )
            )
            info_error = _v5_status_u32(ctypes.get_last_error())
            if not info_ok:
                raise StageCError(
                    "CryptCATCatalogInfoFromContext failed: "
                    f"{ctypes.get_last_error()}"
                )
            path = str(info.wszCatalogFile)
            if not path:
                raise StageCError("catalog enumeration returned an empty path")
            descriptor = {
                "source_ordinal": len(descriptors),
                "catalog_info_path": path,
                "enum_returned_context": True,
                "enum_last_error": 0,
                "catalog_info_returned": info_ok,
                "catalog_info_last_error": info_error,
                "catalog_info_cb_struct": int(info.cbStruct),
                "reserved_flags": 0,
            }
            descriptors.append(descriptor)
            calls.append(dict(descriptor))
    except BaseException as exc:
        primary_error = exc
        evidence["candidate_descriptor_count"] = len(descriptors)
        evidence["clean_end"] = bool(calls and calls[-1].get("clean_end"))
        setattr(exc, "catalog_enumeration_evidence", dict(evidence))
        raise
    finally:
        if previous.value:
            try:
                _v5_release_catalog_context(wintrust, admin, previous)
            except BaseException as release_exc:
                if primary_error is not None:
                    setattr(
                        primary_error,
                        "catalog_enumeration_release_error",
                        str(release_exc),
                    )
                else:
                    setattr(
                        release_exc,
                        "catalog_enumeration_evidence",
                        dict(evidence),
                    )
                    raise
    evidence["candidate_descriptor_count"] = len(descriptors)
    evidence["clean_end"] = bool(calls and calls[-1].get("clean_end"))
    return descriptors, evidence


def _v5_close_held_file(handle: int, *, label: str) -> None:
    kernel32, _ = _v5_catalog_apis()
    if not kernel32.CloseHandle(_v5_handle(handle)):
        raise StageCError(f"CloseHandle({label}) failed: {ctypes.get_last_error()}")


def _v5_candidate_sort_key(candidate: Mapping[str, Any]) -> tuple[Any, ...]:
    identity = candidate["identity"]
    return (
        _norm(os.path.abspath(str(candidate["path"]))),
        int(identity.get("volume_serial_64", 0)),
        bytes.fromhex(str(identity.get("file_id_128", ""))),
        str(identity.get("sha256", "")),
        str(candidate.get("path", "")),
    )


def _v5_compare_catalog_candidates(
    left: Mapping[str, Any], right: Mapping[str, Any]
) -> int:
    compare = ctypes.WinDLL("kernel32", use_last_error=True).CompareStringOrdinal
    compare.argtypes = [wt.LPCWSTR, ctypes.c_int, wt.LPCWSTR, ctypes.c_int, wt.BOOL]
    compare.restype = ctypes.c_int
    left_path = str(left["normalized_path"])
    right_path = str(right["normalized_path"])
    ordinal = int(compare(left_path, -1, right_path, -1, True))
    if ordinal not in (1, 2, 3):
        raise StageCError(f"CompareStringOrdinal failed: {ctypes.get_last_error()}")
    if ordinal != 2:
        return -1 if ordinal == 1 else 1
    left_identity = left["identity"]
    right_identity = right["identity"]
    left_tail = (
        int(left_identity["volume_serial_64"]).to_bytes(8, "big", signed=False),
        bytes.fromhex(str(left_identity["file_id_128"])),
        int(left_identity["bytes"]),
        str(left_identity["sha256"]).lower().encode("ascii"),
    )
    right_tail = (
        int(right_identity["volume_serial_64"]).to_bytes(8, "big", signed=False),
        bytes.fromhex(str(right_identity["file_id_128"])),
        int(right_identity["bytes"]),
        str(right_identity["sha256"]).lower().encode("ascii"),
    )
    if left_tail != right_tail:
        return -1 if left_tail < right_tail else 1
    display = int(compare(str(left["path"]), -1, str(right["path"]), -1, False))
    if display not in (1, 2, 3):
        raise StageCError(f"CompareStringOrdinal(display) failed: {ctypes.get_last_error()}")
    return 0 if display == 2 else -1 if display == 1 else 1


def _v5_validate_catalog_identity(path: str, identity: Mapping[str, Any]) -> None:
    if (
        identity.get("exists") is not True
        or identity.get("directory") is not False
        or identity.get("reparse") is not False
    ):
        raise StageCError(f"catalog candidate is not a held direct file: {path}")
    if _norm(str(identity.get("path", ""))) != _norm(path):
        raise StageCError(f"catalog candidate path identity mismatch: {path}")
    if int(identity.get("volume_serial_64", 0)) <= 0 or not re.fullmatch(
        r"[0-9A-F]{32}", str(identity.get("file_id_128", ""))
    ):
        raise StageCError(f"catalog candidate file ID is incomplete: {path}")
    if int(identity.get("bytes", -1)) < 0:
        raise StageCError(f"catalog candidate byte count is invalid: {path}")
    sha256 = str(identity.get("sha256", ""))
    if len(sha256) != 64 or any(character not in "0123456789abcdefABCDEF" for character in sha256):
        raise StageCError(f"catalog candidate SHA-256 is invalid: {path}")


def _v5_materialize_catalog_candidates(
    descriptors: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    from functools import cmp_to_key

    candidates: list[dict[str, Any]] = []
    by_path: dict[str, dict[str, Any]] = {}
    by_file: dict[tuple[int, str], dict[str, Any]] = {}
    try:
        source_ordinals: set[int] = set()
        for raw_descriptor in descriptors:
            source_ordinal = int(raw_descriptor["source_ordinal"])
            if source_ordinal in source_ordinals:
                raise StageCError("CATALOG_MATERIALIZATION_INVALID: duplicate source ordinal")
            source_ordinals.add(source_ordinal)
            path = str(raw_descriptor["catalog_info_path"])
            if not path:
                raise StageCError("CATALOG_MATERIALIZATION_INVALID: empty path")
            handle = _open_held_direct_file(path)
            try:
                identity = _identity_from_handle(handle, path, include_hash=True)
                _v5_validate_catalog_identity(path, identity)
            except BaseException:
                _v5_close_held_file(handle, label="catalog candidate after identity failure")
                raise
            candidate = {
                "path": path,
                "normalized_path": _norm(os.path.abspath(path)),
                "handle": handle,
                "identity": identity,
                "aliases": [path],
                "source_ordinals": [source_ordinal],
                "raw_descriptors": [dict(raw_descriptor)],
            }
            normalized = _norm(os.path.abspath(path))
            previous_path = by_path.get(normalized)
            if previous_path is not None:
                if not _same_file_identity(previous_path["identity"], identity):
                    _v5_close_held_file(handle, label="conflicting catalog path")
                    raise StageCError(f"CATALOG_IDENTITY_CONFLICT: {path}")
                previous_path["aliases"].append(path)
                previous_path["source_ordinals"].append(source_ordinal)
                previous_path["raw_descriptors"].append(dict(raw_descriptor))
                _v5_close_held_file(handle, label="duplicate catalog path")
                continue
            file_key = (
                int(identity.get("volume_serial_64", -1)),
                str(identity.get("file_id_128", "")),
            )
            if file_key[0] < 0 or not re.fullmatch(r"[0-9A-F]{32}", file_key[1]):
                _v5_close_held_file(handle, label="invalid FILE_ID_INFO identity")
                raise StageCError("CATALOG_MATERIALIZATION_INVALID: missing FILE_ID_INFO")
            previous_file = by_file.get(file_key)
            if previous_file is not None:
                previous_lowest_ordinal = min(previous_file["source_ordinals"])
                if (
                    previous_file["identity"].get("sha256") != identity.get("sha256")
                    or previous_file["identity"].get("bytes") != identity.get("bytes")
                ):
                    _v5_close_held_file(handle, label="conflicting catalog alias")
                    raise StageCError(
                        "CATALOG_IDENTITY_CONFLICT: aliases share a file ID but differ in bytes"
                    )
                previous_file["aliases"].append(path)
                previous_file["source_ordinals"].append(source_ordinal)
                previous_file["raw_descriptors"].append(dict(raw_descriptor))
                if source_ordinal < previous_lowest_ordinal:
                    previous_file["path"] = path
                    previous_file["normalized_path"] = _norm(os.path.abspath(path))
                _v5_close_held_file(handle, label="duplicate catalog alias")
                continue
            by_path[normalized] = candidate
            by_file[file_key] = candidate
            candidates.append(candidate)
        for candidate in candidates:
            if candidate["source_ordinals"] != sorted(candidate["source_ordinals"]):
                raise StageCError("CATALOG_MATERIALIZATION_INVALID: alias order changed")
            candidate["alias_occurrences"] = [
                {"source_ordinal": source_ordinal, "path": alias}
                for source_ordinal, alias in zip(
                    candidate["source_ordinals"], candidate["aliases"], strict=True
                )
            ]
        candidates.sort(key=cmp_to_key(_v5_compare_catalog_candidates))
        return candidates
    except BaseException:
        for candidate in candidates:
            try:
                _v5_close_held_file(candidate["handle"], label="catalog candidate rollback")
            except BaseException:
                pass
        raise


def _v5_catalog_attempt(
    *,
    admin: wt.HANDLE,
    member_hash: bytes,
    member_path: str,
    member_handle: int,
    catalog: Mapping[str, Any],
) -> dict[str, Any]:
    member_buffer = (ctypes.c_ubyte * len(member_hash)).from_buffer_copy(member_hash)
    member_tag = member_hash.hex().upper()
    catalog_info = WINTRUST_CATALOG_INFO()
    catalog_info.cbStruct = ctypes.sizeof(catalog_info)
    catalog_info.dwCatalogVersion = 0
    catalog_info.pcwszCatalogFilePath = str(catalog["path"])
    catalog_info.pcwszMemberTag = member_tag
    catalog_info.pcwszMemberFilePath = member_path
    catalog_info.hMemberFile = _v5_handle(member_handle)
    catalog_info.pbCalculatedFileHash = ctypes.cast(
        member_buffer, ctypes.POINTER(ctypes.c_ubyte)
    )
    catalog_info.cbCalculatedFileHash = len(member_hash)
    catalog_info.pcCatalogContext = None
    catalog_info.hCatAdmin = admin
    return _v5_wintrust_attempt(
        source="catalog",
        union_choice=_V5_WTD_CHOICE_CATALOG,
        union_value=catalog_info,
    )


def _v5_catalog_authenticode_identity(
    path: str,
    held_handle: int,
    held_identity: dict[str, Any],
    events: list[dict[str, Any]],
) -> dict[str, Any]:
    _, wintrust = _v5_catalog_apis()
    admin = wt.HANDLE()
    if not wintrust.CryptCATAdminAcquireContext2(
        ctypes.byref(admin), None, "SHA256", None, 0
    ):
        raise StageCError(
            f"CryptCATAdminAcquireContext2(SHA256) failed: {ctypes.get_last_error()}"
        )
    candidates: list[dict[str, Any]] = []
    candidate_results: list[dict[str, Any]] = []
    catalog_release_proof: dict[str, Any] = {
        "attempted": False,
        "succeeded": False,
        "error": None,
    }
    primary_error: BaseException | None = None
    try:
        try:
            member_hash, hash_evidence = _v5_catalog_hash(admin, held_handle)
        except BaseException as exc:
            _v5_record_c01_event(
                events,
                "catalog_hash",
                {
                    "outcome": "failure",
                    "error": _error_record(exc),
                    "evidence": getattr(exc, "catalog_hash_evidence", None),
                },
            )
            _v5_record_c01_event(
                events,
                "catalog_enumeration",
                {
                    "outcome": "not_started",
                    "stage": "catalog_hash",
                    "error": _error_record(exc),
                    "candidate_count": 0,
                },
            )
            raise
        _v5_record_c01_event(
            events,
            "catalog_hash",
            {
                **hash_evidence,
                "bytes": len(member_hash),
                "sha256": member_hash.hex(),
            },
        )
        try:
            descriptors, enumeration_api = _v5_catalog_paths(admin, member_hash)
        except BaseException as exc:
            _v5_record_c01_event(
                events,
                "catalog_enumeration",
                {
                    "outcome": "failure",
                    "stage": "enumeration_api",
                    "error": _error_record(exc),
                    "raw_api": getattr(exc, "catalog_enumeration_evidence", None),
                    "candidate_count": 0,
                },
            )
            raise
        if not descriptors:
            error = StageCError("catalog enumeration completed cleanly with zero candidates")
            _v5_record_c01_event(
                events,
                "catalog_enumeration",
                {
                    "outcome": "failure",
                    "stage": "clean_zero_candidates",
                    "error": _error_record(error),
                    "raw_api": enumeration_api,
                    "candidate_count": 0,
                },
            )
            raise error
        try:
            candidates = _v5_materialize_catalog_candidates(descriptors)
        except BaseException as exc:
            _v5_record_c01_event(
                events,
                "catalog_enumeration",
                {
                    "outcome": "failure",
                    "stage": "candidate_materialization",
                    "error": _error_record(exc),
                    "raw_api": enumeration_api,
                    "candidate_count": 0,
                    "descriptor_count": len(descriptors),
                },
            )
            raise
        candidate_results = [
            {
                "ordinal": ordinal,
                "path": candidate["path"],
                "identity": candidate["identity"],
                "aliases": candidate["aliases"],
                "source_ordinals": candidate["source_ordinals"],
                "accepted": False,
                "outcome": "not_evaluated",
                "membership": None,
                "candidate_handle_close": {
                    "attempted": False,
                    "succeeded": False,
                    "error": None,
                },
                "catalog_context_release": None,
            }
            for ordinal, candidate in enumerate(candidates)
        ]
        _v5_record_c01_event(
            events,
            "catalog_enumeration",
            {
                "candidate_count": len(candidates),
                "raw_api": enumeration_api,
                "candidates": [
                    {
                        "ordinal": ordinal,
                        "path": candidate["path"],
                        "identity": candidate["identity"],
                        "aliases": candidate["aliases"],
                        "source_ordinals": candidate["source_ordinals"],
                        "raw_descriptors": candidate["raw_descriptors"],
                    }
                    for ordinal, candidate in enumerate(candidates)
                ],
            },
        )
        accepted: list[dict[str, Any]] = []
        for ordinal, candidate in enumerate(candidates):
            candidate_event = candidate_results[ordinal]
            identity_before = _identity_from_handle(
                candidate["handle"], str(candidate["path"]), include_hash=True
            )
            _v5_validate_catalog_identity(str(candidate["path"]), identity_before)
            if not _same_file_identity(identity_before, candidate["identity"]):
                raise StageCError("catalog candidate changed before WinTrust evaluation")
            _v5_record_c01_event(
                events,
                "catalog_candidate_intent",
                {
                    "ordinal": ordinal,
                    "path": candidate["path"],
                    "identity": candidate["identity"],
                    "member_hash": member_hash.hex(),
                },
            )
            try:
                attempt = _v5_catalog_attempt(
                    admin=admin,
                    member_hash=member_hash,
                    member_path=path,
                    member_handle=held_handle,
                    catalog=candidate,
                )
            except BaseException as exc:
                identity_after_error: dict[str, Any] | None = None
                identity_after_error_failure: dict[str, Any] | None = None
                try:
                    identity_after_error = _identity_from_handle(
                        candidate["handle"], str(candidate["path"]), include_hash=True
                    )
                    _v5_validate_catalog_identity(
                        str(candidate["path"]), identity_after_error
                    )
                    if not _same_file_identity(
                        identity_after_error, candidate["identity"]
                    ):
                        raise StageCError(
                            "catalog candidate changed during failed WinTrust evaluation"
                        )
                except BaseException as identity_exc:
                    identity_after_error_failure = _error_record(identity_exc)
                candidate_event.update(
                    {
                        "outcome": "failure",
                        "membership": getattr(exc, "wintrust_attempt", None),
                        "error": _error_record(exc),
                        "identity_before": identity_before,
                        "identity_after_error": identity_after_error,
                        "identity_after_error_failure": identity_after_error_failure,
                        "wintrust_close_proof": (
                            None
                            if getattr(exc, "wintrust_attempt", None) is None
                            else getattr(exc, "wintrust_attempt").get("close_proof")
                        ),
                    }
                )
                if identity_after_error_failure is not None:
                    raise StageCError(
                        "CATALOG_MATERIALIZATION_INVALID: candidate identity changed"
                    ) from exc
                if bool(getattr(exc, "wintrust_close_failed", False)):
                    raise
                continue
            identity_after = _identity_from_handle(
                candidate["handle"], str(candidate["path"]), include_hash=True
            )
            _v5_validate_catalog_identity(str(candidate["path"]), identity_after)
            if not _same_file_identity(identity_after, candidate["identity"]):
                raise StageCError("catalog candidate changed during WinTrust evaluation")
            candidate_event.update(
                {
                    "outcome": "failure" if attempt["status"] != 0 else "evaluated",
                    "membership": attempt,
                    "wintrust_close_proof": attempt["close_proof"],
                    "identity_before": identity_before,
                    "identity_after": identity_after,
                }
            )
            if attempt["status"] != 0:
                candidate_event["error"] = {
                    "type": "WinTrustStatus",
                    "status": attempt["status"],
                    "status_hex": attempt["status_hex"],
                }
            if attempt["status"] == 0:
                try:
                    provider = attempt["provider"]
                    if (
                        provider.get("provider_present") is not True
                        or provider.get("signer_present") is not True
                        or int(provider.get("certificate_count", 0)) < 2
                        or any(
                            int(row.get("error", 0)) != 0
                            for row in provider.get("certificate_errors", [])
                        )
                    ):
                        raise StageCError(
                            "catalog membership provider chain is absent or contains errors"
                        )
                    signer_policy = _v5_validate_microsoft_provider(provider)
                    candidate_event["catalog_signer_policy"] = signer_policy
                    identity_after_policy = _identity_from_handle(
                        candidate["handle"],
                        str(candidate["path"]),
                        include_hash=True,
                    )
                    if not _same_file_identity(
                        identity_after_policy, candidate["identity"]
                    ):
                        raise StageCError(
                            "catalog candidate changed during signer-policy evaluation"
                        )
                    candidate_event["identity_after_policy"] = identity_after_policy
                    candidate_event["accepted"] = True
                    candidate_event["outcome"] = "success"
                    accepted.append(
                        {
                            "ordinal": ordinal,
                            "candidate": candidate,
                            "membership": attempt,
                            "catalog_signer_policy": signer_policy,
                        }
                    )
                except BaseException as exc:
                    candidate_event["outcome"] = "failure"
                    candidate_event["error"] = _error_record(exc)
                    candidate_event["catalog_signer_policy_error"] = {
                        "type": type(exc).__name__,
                        "message_sha256": hashlib.sha256(
                            str(exc).encode("utf-8")
                        ).hexdigest(),
                    }
        if not accepted:
            raise StageCError("no enumerated catalog candidate passed membership and signer policy")
        selected = accepted[0]
        return {
            "path": path,
            "held_identity": held_identity,
            "signature_source": "catalog",
            "member_hash_algorithm": "SHA256",
            "member_hash": member_hash.hex(),
            "candidate_count": len(candidates),
            "accepted_candidate_count": len(accepted),
            "selected_candidate_ordinal": selected["ordinal"],
            "selected_catalog": {
                "path": selected["candidate"]["path"],
                "identity": selected["candidate"]["identity"],
                "membership": selected["membership"],
                "signer_policy": selected["catalog_signer_policy"],
            },
        }
    except BaseException as exc:
        primary_error = exc
        raise
    finally:
        close_errors: list[dict[str, Any]] = []
        for ordinal, candidate in enumerate(candidates):
            close_proof = {
                "attempted": True,
                "succeeded": False,
                "error": None,
            }
            try:
                _v5_close_held_file(candidate["handle"], label="catalog candidate")
                close_proof["succeeded"] = True
            except BaseException as exc:
                close_proof["error"] = _error_record(exc)
                close_errors.append(
                    {"phase": "candidate_handle_close", "ordinal": ordinal, "error": _error_record(exc)}
                )
            if ordinal < len(candidate_results):
                candidate_results[ordinal]["candidate_handle_close"] = close_proof
                if close_proof["succeeded"] is not True:
                    candidate_results[ordinal]["accepted"] = False
                    candidate_results[ordinal]["outcome"] = "failure"
                    candidate_results[ordinal]["error"] = {
                        "type": "CatalogCandidateHandleCloseFailure",
                        "close_error": close_proof["error"],
                    }
        catalog_release_proof["attempted"] = bool(admin.value)
        if admin.value:
            if wintrust.CryptCATAdminReleaseContext(admin, 0):
                catalog_release_proof["succeeded"] = True
            else:
                release_error = StageCError(
                    f"CryptCATAdminReleaseContext failed: {ctypes.get_last_error()}"
                )
                catalog_release_proof["error"] = _error_record(release_error)
                close_errors.append(
                    {"phase": "catalog_context_release", "error": _error_record(release_error)}
                )
        for candidate_event in candidate_results:
            candidate_event["catalog_context_release"] = dict(catalog_release_proof)
            if candidate_event.get("outcome") == "not_evaluated":
                candidate_event["outcome"] = "failure"
                candidate_event["error"] = {
                    "type": "CatalogCandidateNotEvaluated",
                    "primary_error": (
                        None if primary_error is None else _error_record(primary_error)
                    ),
                }
            if close_errors and candidate_event.get("accepted") is True:
                candidate_event["accepted"] = False
                candidate_event["outcome"] = "failure"
                candidate_event["error"] = {
                    "type": "CatalogCleanupFailure",
                    "cleanup_errors": list(close_errors),
                }
            _v5_record_c01_event(
                events,
                "catalog_candidate_result",
                candidate_event,
            )
        if close_errors:
            if primary_error is not None:
                setattr(primary_error, "catalog_cleanup_errors", list(close_errors))
            else:
                cleanup_error = StageCError("catalog candidate/context cleanup failed")
                cleanup_error.catalog_cleanup_errors = list(close_errors)
                raise cleanup_error


def _authenticode_identity(
    path: str,
    held_handle: wt.HANDLE,
    held_identity: dict[str, Any],
    held_direct_proof: dict[str, Any],
) -> dict[str, Any]:
    events: list[dict[str, Any]] = []
    _v5_record_c01_event(
        events,
        "trust_intent",
        {
            "path": path,
            "held_identity": held_identity,
            "held_direct_proof": held_direct_proof,
            "policy": "embedded_first_catalog_only_on_TRUST_E_NOSIGNATURE",
            "api": "WinVerifyTrust/WINTRUST_ACTION_GENERIC_VERIFY_V2",
            "embedded_union_choice": "WTD_CHOICE_FILE",
            "catalog_union_choice": "WTD_CHOICE_CATALOG",
            "ui_choice": _V5_WTD_UI_NONE,
            "revocation_checks": _V5_WTD_REVOKE_WHOLECHAIN,
            "provider_flags": (
                _V5_WTD_REVOCATION_CHECK_CHAIN_EXCLUDE_ROOT
                | _V5_WTD_CACHE_ONLY_URL_RETRIEVAL
                | _V5_WTD_DISABLE_MD2_MD4
            ),
            "embedded_verify_count": 1,
            "deadline_seconds": 30,
            "expected_receipts": [
                "trust_intent.json",
                "embedded_attempt.json",
                "catalog_enumeration.json",
                "catalog_candidates/<ordinal>-<sha256>/candidate_intent.json",
                "catalog_candidates/<ordinal>-<sha256>/candidate_result.json|candidate_failure.json",
                "trust_failure.json|result.json",
            ],
        },
    )
    try:
        embedded = _v5_embedded_attempt(path, held_handle)
    except BaseException as exc:
        _v5_record_c01_event(
            events,
            "embedded_attempt",
            {
                "outcome": "failure",
                "error": _error_record(exc),
                "attempt": getattr(exc, "wintrust_attempt", None),
                "close_proof": (
                    None
                    if getattr(exc, "wintrust_attempt", None) is None
                    else getattr(exc, "wintrust_attempt").get("close_proof")
                ),
            },
        )
        raise
    if embedded["status"] == 0:
        try:
            signer_policy = _v5_validate_microsoft_provider(embedded["provider"])
        except BaseException as exc:
            _v5_record_c01_event(
                events,
                "embedded_attempt",
                {
                    "outcome": "failure",
                    "error": _error_record(exc),
                    "attempt": embedded,
                    "close_proof": embedded["close_proof"],
                },
            )
            raise
        _v5_record_c01_event(
            events,
            "embedded_attempt",
            {
                "outcome": "verified",
                "attempt": embedded,
                "close_proof": embedded["close_proof"],
                "signer_policy": signer_policy,
            },
        )
        return {
            "path": path,
            "held_identity": held_identity,
            "signature_source": "embedded",
            "status": embedded["status"],
            "status_hex": embedded["status_hex"],
            "provider": embedded["provider"],
            "signer_policy": signer_policy,
            "valid_microsoft_signature": True,
            "embedded_attempt": embedded,
            "c01_receipt_events": events,
        }
    _v5_record_c01_event(
        events,
        "embedded_attempt",
        {
            "outcome": "classified_non_success",
            "attempt": embedded,
            "close_proof": embedded["close_proof"],
        },
    )
    if embedded["status"] != _V5_TRUST_E_NOSIGNATURE:
        raise StageCError(
            "embedded WinVerifyTrust failed with a non-fallback status: "
            f"{embedded['status_hex']}"
        )
    _v5_record_c01_event(
        events,
        "catalog_fallback_intent",
        {
            "trigger_status": embedded["status"],
            "trigger_status_hex": embedded["status_hex"],
            "hash_algorithm": "SHA256",
            "acquire_context_flags": 0,
            "hash_sizing_flags": 0,
            "hash_fill_flags": 0,
            "enumeration_flags": 0,
        },
    )
    try:
        result = _v5_catalog_authenticode_identity(
            path, held_handle, held_identity, events
        )
    except (_ReceiptRegistrationLost, _ContainmentProofLost):
        raise
    except BaseException as exc:
        if not any(event.get("kind") == "catalog_enumeration" for event in events):
            _v5_record_c01_event(
                events,
                "catalog_enumeration",
                {
                    "outcome": "failure",
                    "stage": "catalog_context_or_unclassified",
                    "error": _error_record(exc),
                    "candidate_count": 0,
                },
            )
        raise
    result["embedded_attempt"] = embedded
    result["c01_receipt_events"] = events
    return result


def _c01_held_identity_impl(
    campaign_started_ns: int,
) -> dict[str, Any]:
    operation_started_ns = time.monotonic_ns()
    _deadline_guard(campaign_started_ns, operation_started_ns, 30)
    resource_before = _resource_snapshot()
    handle: wt.HANDLE | None = None
    primary_error: BaseException | None = None
    held_direct_proof: dict[str, Any] = {
        "schema": "anysolver.no_numba_residual.stage_c.held_direct_file_proof/1",
        "path": WSL_PATH,
        "share_mode": "FILE_SHARE_READ",
        "open_attempted": True,
        "open_succeeded": False,
        "identity_after_open": None,
        "close_attempted": False,
        "close_succeeded": False,
        "close_error": None,
        "operation_outcome": "pending",
        "started_utc": _utc(),
        "completed_utc": None,
    }
    try:
        handle = _open_held_direct_file(WSL_PATH)
        held_direct_proof["open_succeeded"] = True
        before = _identity_from_handle(handle, WSL_PATH, include_hash=True)
        held_direct_proof["identity_after_open"] = before
        if before["reparse"] or before["directory"]:
            raise StageCError("C01 held wsl.exe identity is not a direct file")
        _deadline_guard(campaign_started_ns, operation_started_ns, 30)
        version = _file_version(WSL_PATH)
        signature = _authenticode_identity(
            WSL_PATH, handle, before, held_direct_proof
        )
        _deadline_guard(campaign_started_ns, operation_started_ns, 30)
        after = _identity_from_handle(handle, WSL_PATH, include_hash=True)
        if before != after:
            raise StageCError("held wsl.exe file identity changed during C01")
        path_after = _path_state(WSL_PATH, include_hash=True)
        for key in ("volume_serial_64", "file_id_128", "bytes", "sha256"):
            if path_after.get(key) != after.get(key):
                raise StageCError(
                    f"wsl.exe path no longer resolves to held identity for {key}"
                )
        resource_after = _resource_snapshot()
        timing = _deadline_guard(campaign_started_ns, operation_started_ns, 30)
        held_direct_proof["operation_outcome"] = "success"
        return {
            "held_file_before": before,
            "held_file_after": after,
            "path_after": path_after,
            "version": version,
            "authenticode": signature,
            "resource_before": resource_before,
            "resource_after": resource_after,
            "timing": timing,
            "held_direct_proof": held_direct_proof,
            "success": True,
        }
    except BaseException as exc:
        primary_error = exc
        held_direct_proof["operation_outcome"] = "failure"
        held_direct_proof["primary_error"] = _error_record(exc)
        setattr(exc, "held_direct_proof", held_direct_proof)
        raise
    finally:
        held_direct_proof["close_attempted"] = handle is not None
        if handle is not None:
            try:
                _close_handle(handle)
                held_direct_proof["close_succeeded"] = True
            except BaseException as close_exc:
                held_direct_proof["close_error"] = _error_record(close_exc)
                if primary_error is None:
                    held_direct_proof["operation_outcome"] = "failure"
                    setattr(close_exc, "held_direct_proof", held_direct_proof)
                    raise
                secondary_errors = list(
                    getattr(primary_error, "secondary_errors", [])
                )
                secondary_errors.append(_error_record(close_exc))
                setattr(primary_error, "secondary_errors", secondary_errors)
        held_direct_proof["completed_utc"] = _utc()


def _atomic_write_bytes(final_path: str, data: bytes) -> dict[str, Any]:
    partial = final_path + ".partial"
    if os.path.lexists(final_path) or os.path.lexists(partial):
        raise StageCError(f"atomic target or partial already exists: {final_path}")
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_BINARY
    fd = os.open(partial, flags, 0o600)
    try:
        view = memoryview(data)
        offset = 0
        while offset < len(view):
            written = os.write(fd, view[offset:])
            if written <= 0:
                raise StageCError(f"short atomic write: {partial}")
            offset += written
        os.fsync(fd)
    finally:
        os.close(fd)
    if not kernel32.MoveFileExW(partial, final_path, MOVEFILE_WRITE_THROUGH):
        raise _win_error(f"MoveFileExW({partial}, {final_path})")
    return {"path": final_path, "bytes": len(data), "sha256": _sha256_bytes(data)}


def _atomic_json_v4(final_path: str, value: dict[str, Any]) -> dict[str, Any]:
    return _atomic_write_bytes(final_path, _canonical_json(value))


_ACTIVE_GLOBAL_RECEIPT_CHAIN: "_GlobalReceiptChain | None" = None


def _v5_receipt_from_final(path: str) -> dict[str, Any]:
    handle = _open_held_direct_file(path)
    primary_error: BaseException | None = None
    try:
        identity = _identity_from_handle(handle, path, include_hash=True)
        if identity["reparse"] or identity["directory"]:
            raise StageCError(f"durable receipt final is not a direct file: {path}")
        return {
            "path": path,
            "bytes": int(identity["bytes"]),
            "sha256": str(identity["sha256"]),
            "volume_serial_64": int(identity["volume_serial_64"]),
            "file_id_128": str(identity["file_id_128"]),
        }
    except BaseException as exc:
        primary_error = exc
        raise
    finally:
        try:
            _close_handle(handle)
        except BaseException as close_exc:
            if primary_error is None:
                raise
            secondary = list(getattr(primary_error, "secondary_errors", []))
            secondary.append(_error_record(close_exc))
            setattr(primary_error, "secondary_errors", secondary)


class _TopLevelPublicationMark(dict[str, Any]):
    """Immutable-in-practice mark staged before a top-level state commit."""


class _GlobalReceiptChain:
    """Serialized receipt chronology plus contained-run reservations and proofs."""

    def __init__(self, directory: str) -> None:
        self.directory = directory
        self.head: dict[str, Any] | None = None
        self.nodes: list[dict[str, Any]] = []
        self.sequence = 0
        self.attempt_id: str | None = None
        self._runs: dict[str, dict[str, Any]] = {}
        self._run_material_hashes: set[str] = set()
        self._run_ordinals: set[tuple[int, str]] = set()
        self._consumer_paths: dict[str, tuple[str, str]] = {}

    def register(
        self,
        artifact: Mapping[str, Any],
        payload: Mapping[str, Any],
    ) -> dict[str, Any]:
        artifact_ref = _receipt_ref(dict(artifact))
        prior_ref = None if self.head is None else dict(self.head)
        node_record: dict[str, Any] | None = None
        attempted_consumer_id: str | None = None
        attempted_run_id: str | None = None
        pending_consumer: tuple[dict[str, Any], str] | None = None
        staged_attempt_id = self.attempt_id
        phase = str(payload.get("phase", payload.get("schema", "receipt")))
        try:
            consumer_binding = self._consumer_paths.get(
                _norm(str(artifact_ref["path"]))
            )
            if consumer_binding is not None:
                attempted_run_id, attempted_consumer_id = consumer_binding
                run = self.require_contained_run(attempted_run_id)
                if attempted_consumer_id in run["observed_consumer_ids"]:
                    raise StageCError(
                        "duplicate contained-run consumer registration: "
                        f"{attempted_consumer_id}"
                    )
                pending_consumer = (run, attempted_consumer_id)
            payload_attempt_id = payload.get("attempt_id")
            if payload_attempt_id is not None:
                if staged_attempt_id is None:
                    staged_attempt_id = str(payload_attempt_id)
                elif staged_attempt_id != str(payload_attempt_id):
                    raise StageCError("global receipt attempt ID changed")
            reopened_artifact = _v5_receipt_from_final(str(artifact_ref["path"]))
            if _receipt_ref(reopened_artifact) != artifact_ref:
                raise StageCError("promoted artifact changed before chain registration")
            declared_predecessor = payload.get("predecessor")
            expected_predecessor = (
                None if prior_ref is None else _receipt_ref(prior_ref)
            )
            predecessor_matches = (
                declared_predecessor is None and expected_predecessor is None
            ) or (
                isinstance(declared_predecessor, Mapping)
                and expected_predecessor is not None
                and _receipt_ref(dict(declared_predecessor))
                == _receipt_ref(dict(expected_predecessor))
            )
            if not predecessor_matches:
                raise StageCError(
                    "receipt predecessor does not equal the current global head: "
                    f"{declared_predecessor!r} != {expected_predecessor!r}"
                )
            sequence = self.sequence + 1
            leaf = os.path.basename(str(artifact_ref["path"]))
            safe_leaf = "".join(
                character
                if character.isalnum() or character in ("-", "_", ".")
                else "_"
                for character in leaf
            )
            node_path = os.path.join(
                self.directory, f"{sequence:06d}_{safe_leaf}.chain.json"
            )
            run_context: dict[str, Any] | None = None
            if pending_consumer is not None:
                run, consumer_id = pending_consumer
                run_context = {
                    "run_id": attempted_run_id,
                    "run_identity_material_sha256": run["material_sha256"],
                    "attempted_consumer_id": consumer_id,
                    "terminal_proof_identity": run.get("terminal_proof_identity"),
                }
            node_payload = {
                "schema": SCHEMA_GLOBAL_RECEIPT_NODE,
                "sequence": sequence,
                "phase": phase,
                "receipt": {
                    **artifact_ref,
                    "schema": payload.get("schema"),
                },
                "predecessor": expected_predecessor,
                "attempted_consumer_id": attempted_consumer_id,
                "run_context": run_context,
                "registered_utc": _utc(),
            }
            node_record = _atomic_json_v4(
                node_path,
                node_payload,
            )
            reopened_node = _v5_receipt_from_final(str(node_record["path"]))
            if _receipt_ref(reopened_node) != _receipt_ref(node_record):
                raise StageCError("global chain node changed after promotion")
            staged_runs = dict(self._runs)
            if pending_consumer is not None:
                run, consumer_id = pending_consumer
                staged_run = dict(run)
                staged_run["observed_consumer_ids"] = [
                    *run["observed_consumer_ids"],
                    consumer_id,
                ]
                staged_run["consumer_receipts"] = [
                    *run["consumer_receipts"],
                    {"consumer_id": consumer_id, "receipt": artifact_ref},
                ]
                staged_runs[str(run["run_id"])] = staged_run
            staged_nodes = [
                *self.nodes,
                {
                    **node_payload,
                    "node_receipt": _receipt_ref(node_record),
                    "committed_consumer_id": attempted_consumer_id,
                },
            ]
            staged_head = {
                **artifact_ref,
                "schema": payload.get("schema"),
                "sequence": sequence,
                "predecessor": expected_predecessor,
            }
            self._runs, self.nodes, self.sequence, self.head, self.attempt_id = (
                staged_runs,
                staged_nodes,
                sequence,
                staged_head,
                staged_attempt_id,
            )
            return node_record
        except BaseException as exc:
            promoted = artifact_ref
            if node_record is not None:
                promoted = _receipt_ref(node_record)
            lost = _ReceiptRegistrationLost(
                phase=phase,
                promoted_receipt=promoted,
                prior_receipt=prior_ref,
                cause=exc,
                containment=None,
                run_id=attempted_run_id or payload.get("run_id"),
                attempted_consumer_id=attempted_consumer_id,
                attempt_id=staged_attempt_id,
                durable_head=prior_ref,
            )
            lost.source_artifact = dict(artifact_ref)
            lost.failing_site = _prejob_site_for_path(str(artifact_ref["path"]))
            raise lost from exc

    def reserve_contained_run(
        self,
        material: Mapping[str, Any],
        consumer_paths: Mapping[str, str],
    ) -> dict[str, Any]:
        material_bytes = _canonical_json_no_lf(dict(material))
        run_id = _derive_contained_run_id(material)
        material_sha256 = hashlib.sha256(material_bytes).hexdigest()
        ordinal = int(material["invocation_ordinal"])
        check_id = str(material["check_id"])
        ordinal_key = (ordinal, check_id)
        if (
            run_id in self._runs
            or material_sha256 in self._run_material_hashes
            or ordinal_key in self._run_ordinals
        ):
            raise StageCError("CONTAINED_RUN_ID_COLLISION")
        normalized_paths: dict[str, str] = {}
        for path, consumer_id in consumer_paths.items():
            normalized = _norm(path)
            if normalized in self._consumer_paths or normalized in normalized_paths:
                raise StageCError("CONTAINED_RUN_CONSUMER_PATH_COLLISION")
            normalized_paths[normalized] = consumer_id
        context = {
            "run_id": run_id,
            "check_id": check_id,
            "invocation_ordinal": ordinal,
            "material": dict(material),
            "material_bytes": material_bytes,
            "material_sha256": material_sha256,
            "observed_consumer_ids": [],
            "consumer_receipts": [],
            "expected_consumer_ids": None,
            "terminal_proof": None,
            "terminal_proof_identity": None,
            "finalized": False,
        }
        self._runs[run_id] = context
        self._run_material_hashes.add(material_sha256)
        self._run_ordinals.add(ordinal_key)
        for path, consumer_id in normalized_paths.items():
            self._consumer_paths[path] = (run_id, consumer_id)
        return context

    def require_contained_run(self, run_id: str) -> dict[str, Any]:
        if not re.fullmatch(r"[0-9a-f]{64}", run_id):
            raise StageCError(f"invalid contained run ID: {run_id!r}")
        try:
            return self._runs[run_id]
        except KeyError as exc:
            raise StageCError(f"contained run is not reserved: {run_id}") from exc

    def retain_contained_terminal_proof(
        self, run_id: str, proof: Mapping[str, Any]
    ) -> dict[str, Any]:
        run = self.require_contained_run(run_id)
        if run["terminal_proof"] is not None:
            raise StageCError(f"contained terminal proof already retained: {run_id}")
        frozen = json.loads(_canonical_json(dict(proof)).decode("utf-8"))
        if (
            frozen.get("run_id") != run_id
            or frozen.get("terminal") is not True
            or frozen.get("zero_pid") is not True
            or frozen.get("handles_closed") is not True
        ):
            raise StageCError("contained terminal proof is incomplete")
        identity = {
            "schema": frozen.get("schema"),
            "bytes": len(_canonical_json(frozen)),
            "sha256": hashlib.sha256(_canonical_json(frozen)).hexdigest().upper(),
        }
        run["terminal_proof"] = frozen
        run["terminal_proof_identity"] = identity
        return frozen

    def require_contained_terminal_proof(self, run_id: str) -> dict[str, Any]:
        run = self.require_contained_run(run_id)
        proof = run.get("terminal_proof")
        if not isinstance(proof, dict):
            raise StageCError(f"contained terminal proof is unavailable: {run_id}")
        return dict(proof)

    def mark_contained_proof_consumed(
        self, run_id: str, expected_consumer_ids: Sequence[str]
    ) -> dict[str, Any]:
        run = self.require_contained_run(run_id)
        self.require_contained_terminal_proof(run_id)
        observed = list(run["observed_consumer_ids"])
        expected = list(expected_consumer_ids)
        if observed != expected:
            raise StageCError(
                f"contained-run consumer sequence mismatch: {observed!r} != {expected!r}"
            )
        if run["finalized"]:
            raise StageCError(f"contained-run proof was already consumed: {run_id}")
        run["expected_consumer_ids"] = expected
        run["finalized"] = True
        return self.run_summary(run_id)

    def freeze_contained_consumer_lane(
        self, run_id: str, expected_consumer_ids: Sequence[str]
    ) -> dict[str, Any]:
        run = self.require_contained_run(run_id)
        self.require_contained_terminal_proof(run_id)
        expected = list(expected_consumer_ids)
        if run["expected_consumer_ids"] is not None:
            raise StageCError(f"contained-run consumer lane already frozen: {run_id}")
        observed = list(run["observed_consumer_ids"])
        if observed != expected[: len(observed)]:
            raise StageCError("contained-run observed consumers are not an expected prefix")
        run["expected_consumer_ids"] = expected
        return self.run_summary(run_id)

    def mark_top_level_publication(
        self,
        run_id: str,
        consumer_id: str,
        terminal_receipt: Mapping[str, Any],
    ) -> dict[str, Any]:
        prior = None if self.head is None else dict(self.head)
        promoted = _receipt_ref(dict(terminal_receipt))
        try:
            reopened = _v5_receipt_from_final(str(promoted["path"]))
            if _receipt_ref(reopened) != promoted:
                raise StageCError("top-level terminal changed before publication mark")
            run = self.require_contained_run(run_id)
            if run["finalized"]:
                raise StageCError(f"contained-run top-level mark is duplicate: {run_id}")
            expected = run.get("expected_consumer_ids")
            if not isinstance(expected, list):
                raise StageCError("contained-run lane was not frozen before terminal")
            observed = list(run["observed_consumer_ids"])
            if observed + [consumer_id] != expected:
                raise StageCError("top-level consumer does not complete the frozen lane")
            mark = _TopLevelPublicationMark(
                consumer_id=consumer_id,
                top_level_publication_mark=promoted,
                attempted_consumer_id=consumer_id,
                committed=True,
            )
            staged_run = dict(run)
            staged_run["observed_consumer_ids"] = [*observed, consumer_id]
            staged_run["consumer_receipts"] = [
                *run["consumer_receipts"],
                dict(mark),
            ]
            staged_run["finalized"] = True
            staged_runs = dict(self._runs)
            staged_runs[run_id] = staged_run
            self._runs = staged_runs
            return self.run_summary(run_id)
        except (_ReceiptRegistrationLost, _ContainmentProofLost):
            raise
        except BaseException as exc:
            lost = _ReceiptRegistrationLost(
                phase="top_level_publication_mark",
                promoted_receipt=promoted,
                prior_receipt=prior,
                cause=exc,
                containment=None,
                run_id=run_id,
                attempted_consumer_id=consumer_id,
                attempt_id=self.attempt_id,
                durable_head=prior,
            )
            raise lost from exc

    def run_summary(self, run_id: str) -> dict[str, Any]:
        run = self.require_contained_run(run_id)
        return {
            "run_id": run_id,
            "check_id": run["check_id"],
            "invocation_ordinal": run["invocation_ordinal"],
            "run_identity_material_sha256": run["material_sha256"],
            "observed_consumer_ids": list(run["observed_consumer_ids"]),
            "expected_consumer_ids": (
                None
                if run["expected_consumer_ids"] is None
                else list(run["expected_consumer_ids"])
            ),
            "consumer_receipts": list(run["consumer_receipts"]),
            "terminal_proof_identity": run["terminal_proof_identity"],
            "finalized": bool(run["finalized"]),
        }

    def summary(self) -> dict[str, Any]:
        return {
            "schema": "anysolver.no_numba_residual.provider_stage_c_global_receipt_chain/1",
            "count": self.sequence,
            "head": None if self.head is None else dict(self.head),
            "nodes": list(self.nodes),
            "contained_runs": [
                self.run_summary(run_id) for run_id in sorted(self._runs)
            ],
            "attempt_id": self.attempt_id,
        }


def _promoted_identity_after_failure(final_path: str, data: bytes) -> dict[str, Any]:
    identity: dict[str, Any] = {
        "path": final_path,
        "bytes": len(data),
        "sha256": _sha256_bytes(data),
    }
    try:
        actual_size, actual_sha256 = _sha256_file(final_path)
        identity["actual_bytes"] = actual_size
        identity["actual_sha256"] = actual_sha256
    except BaseException as exc:
        identity["actual_identity_error"] = _error_record(exc)
    return identity


def _atomic_json(final_path: str, value: dict[str, Any]) -> dict[str, Any]:
    data = _canonical_json(value)
    try:
        record = _atomic_write_bytes(final_path, data)
    except (_ReceiptRegistrationLost, _ContainmentProofLost):
        raise
    except BaseException as exc:
        if os.path.lexists(final_path):
            chain = _ACTIVE_GLOBAL_RECEIPT_CHAIN
            raise _ReceiptRegistrationLost(
                phase=str(value.get("phase", value.get("schema", "json_promotion"))),
                promoted_receipt=_promoted_identity_after_failure(final_path, data),
                prior_receipt=(
                    None if chain is None or chain.head is None else dict(chain.head)
                ),
                cause=exc,
                containment=None,
            ) from exc
        raise _AtomicJsonPrePromotionFailure(final_path, exc) from exc
    chain = _ACTIVE_GLOBAL_RECEIPT_CHAIN
    if chain is not None:
        chain.register(record, value)
    return record


def _atomic_terminal_json(final_path: str, value: dict[str, Any]) -> dict[str, Any]:
    """Publish the one top-level terminal outside the chain it contains."""

    data = _canonical_json(value)
    chain = _ACTIVE_GLOBAL_RECEIPT_CHAIN
    prior = None if chain is None or chain.head is None else dict(chain.head)
    try:
        record = _atomic_write_bytes(final_path, data)
    except BaseException as exc:
        if not os.path.lexists(final_path):
            raise _AtomicJsonPrePromotionFailure(final_path, exc) from exc
        raise _ReceiptRegistrationLost(
            phase="top_level_terminal_promotion",
            promoted_receipt=_promoted_identity_after_failure(final_path, data),
            prior_receipt=prior,
            cause=exc,
            containment=None,
        ) from exc
    try:
        reopened = _v5_receipt_from_final(final_path)
        if _receipt_ref(reopened) != _receipt_ref(record):
            raise StageCError("top-level terminal changed after atomic promotion")
        raw = open(final_path, "rb").read()
        parsed = json.loads(raw.decode("utf-8"))
        if raw != data or parsed.get("schema") != value.get("schema"):
            raise StageCError("top-level terminal reopen/schema validation failed")
    except BaseException as exc:
        raise _ReceiptRegistrationLost(
            phase="top_level_terminal_reopen",
            promoted_receipt=_promoted_identity_after_failure(final_path, data),
            prior_receipt=prior,
            cause=exc,
            containment=None,
        ) from exc
    return record


_V5_INTERNAL_SUCCESS_CONSUMERS = (
    "job_intent.json",
    "creation_attributes_intent.json",
    "job_configured.json",
    "creation_attributes_ready.json",
    "assigned_at_creation_before_resume.json",
    "stdout.bin",
    "stderr.bin",
    "creation_attributes_final.json",
    "process.json",
    "job_process.json",
)
_V5_INTERNAL_FAILURE_CONSUMERS = (
    "process_failure.json",
    "job_process_failure.json",
)


def _derive_contained_run_id(material: Mapping[str, Any]) -> str:
    required = {
        "schema",
        "v5_sha256",
        "campaign_intent_sha256",
        "attempt_id",
        "check_id",
        "invocation_ordinal",
        "predecessor_sha256",
        "argv_sha256",
        "environment_manifest_sha256",
    }
    if set(material) != required:
        raise StageCError("contained run identity material keys are not exact")
    if material["schema"] != (
        "anysolver.no_numba_residual.stage_c.contained_run_identity_material/1"
    ):
        raise StageCError("contained run identity material schema mismatch")
    for key in (
        "v5_sha256",
        "campaign_intent_sha256",
        "predecessor_sha256",
        "argv_sha256",
        "environment_manifest_sha256",
    ):
        if not re.fullmatch(r"[0-9A-F]{64}", str(material[key])):
            raise StageCError(f"contained run identity hash is invalid: {key}")
    return hashlib.sha256(_canonical_json_no_lf(dict(material))).hexdigest()


def _canonical_json_no_lf(value: Any) -> bytes:
    encoded = _canonical_json(value)
    if not encoded.endswith(b"\n") or encoded.endswith(b"\n\n"):
        raise StageCError("canonical JSON did not have exactly one terminal LF")
    return encoded[:-1]


def _v5_reserve_run(
    check_id: str,
    argv: Sequence[str],
    check_dir: str,
    common: Mapping[str, Any],
    predecessor: dict[str, Any],
) -> dict[str, Any]:
    chain = _ACTIVE_GLOBAL_RECEIPT_CHAIN
    if chain is None:
        raise StageCError("contained run cannot be reserved without a global chain")
    check_ids = [row[0] for row in CHECKS[1:]]
    if check_id not in check_ids:
        raise StageCError(f"run reservation is not defined for check {check_id!r}")
    expected_dir = os.path.join(str(common.get("evidence_root", "")), "checks", check_id)
    if _norm(check_dir) != _norm(expected_dir):
        raise StageCError("run reservation check directory is not canonical")
    frozen_argv = dict((row[0], row[1]) for row in CHECKS)[check_id]
    if list(argv) != list(frozen_argv):
        raise StageCError("run reservation argv is not the frozen check argv")
    predecessor_ref = _receipt_ref(dict(predecessor))
    _, environment_record = _child_environment()
    material = {
        "schema": "anysolver.no_numba_residual.stage_c.contained_run_identity_material/1",
        "v5_sha256": str(common["packet"]["sha256"]),
        "campaign_intent_sha256": str(common["campaign_intent"]["sha256"]),
        "attempt_id": str(common["attempt_id"]),
        "check_id": check_id,
        "invocation_ordinal": check_ids.index(check_id),
        "predecessor_sha256": str(predecessor_ref["sha256"]),
        "argv_sha256": _sha256_bytes(_canonical_json_no_lf(list(argv))),
        "environment_manifest_sha256": _sha256_bytes(
            _canonical_json_no_lf(environment_record)
        ),
    }
    run_id = _derive_contained_run_id(material)
    internal_ids = {
        os.path.join(check_dir, name): f"run:{run_id}:internal:{name}"
        for name in _V5_INTERNAL_SUCCESS_CONSUMERS + _V5_INTERNAL_FAILURE_CONSUMERS
    }
    internal_ids[os.path.join(check_dir, "result.json")] = (
        f"run:{run_id}:outer-result"
    )
    internal_ids[
        os.path.join(str(common["evidence_root"]), "snapshots", f"post_{check_id}.json")
    ] = f"run:{run_id}:post-check-snapshot"
    if check_id == "C05":
        internal_ids[
            os.path.join(str(common["evidence_root"]), "snapshots", "final.json")
        ] = f"run:{run_id}:campaign-final-snapshot"
    context = chain.reserve_contained_run(material, internal_ids)
    if context["run_id"] != run_id:
        raise StageCError("caller/callee contained run ID disagreement")
    context["check_dir"] = check_dir
    return context


def _v5_finalize_run_consumers(
    context: dict[str, Any],
    *,
    lane: str,
    outer_receipts: Sequence[tuple[str, Mapping[str, Any]]] = (),
    failure_final_count: int | None = None,
) -> dict[str, Any]:
    chain = _ACTIVE_GLOBAL_RECEIPT_CHAIN
    if chain is None:
        raise StageCError("run consumers cannot finalize without a global chain")
    run = chain.require_contained_run(str(context["run_id"]))
    observed = list(run["observed_consumer_ids"])
    internal_success = [
        f"run:{context['run_id']}:internal:{name}"
        for name in _V5_INTERNAL_SUCCESS_CONSUMERS
    ]
    internal_failure = [
        f"run:{context['run_id']}:internal:{name}"
        for name in _V5_INTERNAL_FAILURE_CONSUMERS
    ]
    outer_ids = [name for name, _ in outer_receipts]
    completed_success = internal_success + [
        f"run:{context['run_id']}:outer-result",
        f"run:{context['run_id']}:post-check-snapshot",
    ]
    if lane == "success":
        if outer_ids != ["result.json", "post_snapshot.json"]:
            raise StageCError("successful run outer consumer order is not exact")
        if observed != completed_success:
            raise StageCError(
                f"successful run consumer state mismatch: {observed!r}"
            )
        if context["check_id"] == "C05":
            return chain.run_summary(str(context["run_id"]))
        return chain.mark_contained_proof_consumed(
            str(context["run_id"]), completed_success
        )
    elif lane == "failure":
        if outer_receipts:
            raise StageCError("failed run cannot claim outer success consumers")
        count = len(internal_failure) if failure_final_count is None else failure_final_count
        if count not in (0, 1, 2):
            raise StageCError("failed run final count must be exactly 0, 1, or 2")
        failure_suffix = internal_failure[:count]
        if count and (
            len(observed) < count or observed[-count:] != failure_suffix
        ):
            raise StageCError("failed run does not match its durable failure-final prefix")
        success_prefix = observed if count == 0 else observed[:-count]
        if success_prefix != internal_success[: len(success_prefix)]:
            raise StageCError("failed run internal success prefix is not exact")
        expected = observed + [f"run:{context['run_id']}:top-level-failure-published"]
        return chain.freeze_contained_consumer_lane(str(context["run_id"]), expected)
    elif lane == "postprocess_failure":
        if outer_ids not in (
            [],
            ["result.json"],
            ["result.json", "post_snapshot.json"],
        ):
            raise StageCError(
                "post-process failure outer consumers are not an exact durable prefix"
            )
        expected_observed = internal_success
        if outer_ids:
            expected_observed = [
                *expected_observed,
                f"run:{context['run_id']}:outer-result",
            ]
        if len(outer_ids) == 2:
            expected_observed = [
                *expected_observed,
                f"run:{context['run_id']}:post-check-snapshot",
            ]
        allowed = [expected_observed]
        if context["check_id"] == "C05":
            allowed.append(
                expected_observed
                + [f"run:{context['run_id']}:campaign-final-snapshot"]
            )
        if observed not in allowed:
            raise StageCError(
                f"post-process failure consumer state is not an exact lane: {observed!r}"
            )
        expected = observed + [f"run:{context['run_id']}:top-level-failure-published"]
        return chain.freeze_contained_consumer_lane(str(context["run_id"]), expected)
    elif lane == "c05_success":
        if context["check_id"] != "C05" or outer_receipts:
            raise StageCError("C05 success finalization arguments are not exact")
        expected_observed = completed_success + [
            f"run:{context['run_id']}:campaign-final-snapshot"
        ]
        if observed != expected_observed:
            raise StageCError("C05 success is missing its exact final-snapshot consumer")
        return chain.freeze_contained_consumer_lane(
            str(context["run_id"]),
            expected_observed
            + [f"run:{context['run_id']}:top-level-success-published"],
        )
    else:
        raise StageCError(f"unknown run consumer lane: {lane}")


def _v5_contained_terminal_proof(
    run_id: str,
    state: Mapping[str, Any],
    *,
    owner_scope: str,
    reason: str,
) -> dict[str, Any]:
    process_created = bool(state.get("process_created"))
    zero_pid = bool(
        state.get("zero_job_processes")
        or state.get("zero_pid_proven_at_failure")
        or state.get("timeout_zero_pid_proven")
    )
    terminal = bool(
        not process_created
        or (
            state.get("exit_code") is not None
            and int(state.get("exit_code")) != STILL_ACTIVE
            and zero_pid
        )
        or (
            state.get("exit_code_at_failure") is not None
            and int(state.get("exit_code_at_failure")) != STILL_ACTIVE
            and zero_pid
        )
    )
    retained = state.get("retained_handles_at_failure_publication", {})
    handles_closed = bool(state.get("handles_closed")) or (
        isinstance(retained, Mapping)
        and not any(bool(value) for value in retained.values())
    )
    proof = {
        "schema": "anysolver.no_numba_residual.stage_c.contained_process_terminal_proof/1",
        "run_id": run_id,
        "owner_scope": owner_scope,
        "reason": reason,
        "child_created": process_created,
        "terminal": terminal,
        "zero_pid": zero_pid,
        "handles_closed": handles_closed,
        "job_identity": state.get("job_handle_identity"),
        "pid": state.get("pid"),
        "process_creation_identity": state.get("process_creation_identity"),
        "exit_code": state.get("exit_code", state.get("exit_code_at_failure")),
        "containment_actions": [
            key
            for key in (
                "termination_reason",
                "termination_returned",
                "timeout_terminal_wait",
                "failure_terminal_wait",
                "zero_pid_proven_at_failure",
            )
            if key in state
        ],
        "containment_errors": [
            value
            for key, value in state.items()
            if key.endswith("_error") or key == "containment_error"
        ],
        "terminal_utc": _utc(),
    }
    if not terminal or not zero_pid or not handles_closed:
        raise _ContainmentProofLost(
            phase="contained_terminal_proof",
            run_id=run_id,
            durable_head=(
                None
                if _ACTIVE_GLOBAL_RECEIPT_CHAIN is None
                or _ACTIVE_GLOBAL_RECEIPT_CHAIN.head is None
                else dict(_ACTIVE_GLOBAL_RECEIPT_CHAIN.head)
            ),
            promoted_receipt=None,
            cause=StageCError("contained terminal proof is incomplete"),
            containment=proof,
        )
    return proof


def _v5_retain_contained_terminal_proof(
    run_id: str,
    state: Mapping[str, Any],
    *,
    owner_scope: str,
    reason: str,
) -> dict[str, Any]:
    chain = _ACTIVE_GLOBAL_RECEIPT_CHAIN
    if chain is None:
        raise StageCError("contained terminal proof has no global chain owner")
    run = chain.require_contained_run(run_id)
    if run.get("terminal_proof") is not None:
        return chain.require_contained_terminal_proof(run_id)
    proof = _v5_contained_terminal_proof(
        run_id, state, owner_scope=owner_scope, reason=reason
    )
    return chain.retain_contained_terminal_proof(run_id, proof)


def _v5_attach_retained_proof(
    fatal: _ReceiptRegistrationLost | _ContainmentProofLost,
    run_id: str,
) -> None:
    chain = _ACTIVE_GLOBAL_RECEIPT_CHAIN
    if chain is None:
        raise StageCError("fatal contained outcome has no global chain")
    proof = chain.require_contained_terminal_proof(run_id)
    fatal.run_id = run_id
    fatal.containment = {
        "owner": proof["owner_scope"],
        "reason": proof["reason"],
        "child_created": proof["child_created"],
        "terminal": proof["terminal"],
        "zero_pid": proof["zero_pid"],
        "handles_closed": proof["handles_closed"],
        "job_identity": proof["job_identity"],
        "pid": proof["pid"],
        "process_creation_identity": proof["process_creation_identity"],
        "containment_errors": proof["containment_errors"],
    }


def _mkdir_new(path: str) -> None:
    if os.path.lexists(path):
        raise StageCError(f"directory already exists: {path}")
    os.mkdir(path)
    state = _path_state(path)
    if not state["directory"] or state["reparse"]:
        raise StageCError(f"created evidence directory is not direct: {path}")


def _c01_held_identity(*args: Any, **kwargs: Any) -> dict[str, Any]:
    with _HardDeadline(30.0, 0xE000C010, "C01"):
        result = _c01_held_identity_impl(*args, **kwargs)
    trusted = _campaign_wsl_identity()
    identities: list[dict[str, Any]] = []

    def collect(value: Any) -> None:
        if isinstance(value, dict):
            if all(
                key in value
                for key in ("volume_serial_64", "file_id_128", "bytes", "sha256")
            ):
                identities.append(value)
            for child in value.values():
                collect(child)
        elif isinstance(value, list):
            for child in value:
                collect(child)

    collect(result)
    wsl_rows = [
        row
        for row in identities
        if _norm(str(row.get("path", ""))) == _norm(WSL_PATH)
    ]
    if not wsl_rows or any(not _same_file_identity(row, trusted) for row in wsl_rows):
        raise StageCError("C01 evidence is not bound to the campaign-held wsl.exe identity")
    return result


_CAMPAIGN_WSL_HANDLE: wt.HANDLE | None = None
_CAMPAIGN_WSL_FROZEN_IDENTITY: dict[str, Any] | None = None


def _acquire_campaign_wsl_hold() -> dict[str, Any]:
    global _CAMPAIGN_WSL_HANDLE, _CAMPAIGN_WSL_FROZEN_IDENTITY
    if _CAMPAIGN_WSL_HANDLE is not None or _CAMPAIGN_WSL_FROZEN_IDENTITY is not None:
        raise StageCError("campaign wsl.exe hold is already active")
    handle = _open_held_direct_file(WSL_PATH)
    try:
        identity = _identity_from_handle(handle, WSL_PATH, include_hash=True)
        if identity.get("directory") or identity.get("reparse"):
            raise StageCError("campaign wsl.exe hold is not a direct file")
    except BaseException:
        kernel32.CloseHandle(handle)
        raise
    _CAMPAIGN_WSL_HANDLE = handle
    _CAMPAIGN_WSL_FROZEN_IDENTITY = identity
    return dict(identity)


def _campaign_wsl_identity() -> dict[str, Any]:
    if _CAMPAIGN_WSL_HANDLE is None or _CAMPAIGN_WSL_FROZEN_IDENTITY is None:
        raise StageCError("campaign wsl.exe hold is not active")
    current = _identity_from_handle(
        _CAMPAIGN_WSL_HANDLE, WSL_PATH, include_hash=True
    )
    if not _same_file_identity(current, _CAMPAIGN_WSL_FROZEN_IDENTITY):
        raise StageCError("campaign-held wsl.exe identity changed")
    return current


def _release_campaign_wsl_hold() -> None:
    global _CAMPAIGN_WSL_HANDLE, _CAMPAIGN_WSL_FROZEN_IDENTITY
    handle = _CAMPAIGN_WSL_HANDLE
    if handle is not None and not kernel32.CloseHandle(handle):
        raise _win_error("CloseHandle(campaign wsl.exe hold)")
    _CAMPAIGN_WSL_HANDLE = None
    _CAMPAIGN_WSL_FROZEN_IDENTITY = None


def _registered_absence_snapshot() -> dict[str, Any]:
    return {
        "builder_import": _require_absent_leaf(BUILDER_IMPORT),
        "final_import": _require_absent_leaf(FINAL_IMPORT),
        "provider_archive": _require_absent_leaf(PROVIDER_ARCHIVE),
        "provider_archive_partial": _require_absent_leaf(PROVIDER_ARCHIVE + ".partial"),
    }


def _process_snapshot_with_file_ids() -> list[dict[str, Any]]:
    rows = _process_snapshot()
    for row in rows:
        image = row.get("image") or row.get("image_path") or row.get("executable")
        if type(image) is not str or not image:
            row["image_file_identity"] = None
            continue
        try:
            identity = _path_state(image, include_hash=False)
            row["image_file_identity"] = {
                key: identity.get(key)
                for key in (
                    "path",
                    "exists",
                    "directory",
                    "reparse",
                    "volume_serial",
                    "file_index",
                    "bytes",
                    "write_filetime",
                )
            }
        except BaseException as exc:
            row["image_file_identity"] = {
                "path": image,
                "evidence_limited": f"{type(exc).__name__}: {exc}",
            }
    return rows


def _host_snapshot(
    label: str,
    include_os: bool,
    predecessor: dict[str, Any],
) -> dict[str, Any]:
    result = {
        "schema": SCHEMA_SNAPSHOT,
        "label": label,
        "predecessor": _receipt_ref(predecessor),
        "utc": _utc(),
        "paths": _registered_absence_snapshot(),
        "wsl_file": _path_state(WSL_PATH, include_hash=False),
        "services": _service_snapshot(),
        "processes": _process_snapshot_with_file_ids(),
        "os_identity": _os_identity() if include_os else None,
        "resources": _resource_snapshot(),
    }
    stable_identity = {
        "paths": result["paths"],
        "wsl_file": result["wsl_file"],
        "os_identity": result["os_identity"],
    }
    result["registered_state_sha256"] = _sha256_bytes(_canonical_json(stable_identity))
    return result


def _job_limits(handle: wt.HANDLE) -> dict[str, Any]:
    info = JOBOBJECT_EXTENDED_LIMIT_INFORMATION()
    returned = wt.DWORD()
    if not kernel32.QueryInformationJobObject(
        handle,
        JOB_OBJECT_EXTENDED_LIMIT_INFORMATION,
        ctypes.byref(info),
        ctypes.sizeof(info),
        ctypes.byref(returned),
    ):
        raise _win_error("QueryInformationJobObject(extended)")
    basic = info.BasicLimitInformation

    def scalar(value: Any) -> int:
        return int(getattr(value, "QuadPart", value))

    result = {
        "per_process_user_time_limit": scalar(basic.PerProcessUserTimeLimit),
        "per_job_user_time_limit": scalar(basic.PerJobUserTimeLimit),
        "limit_flags": int(basic.LimitFlags),
        "minimum_working_set_size": int(basic.MinimumWorkingSetSize),
        "maximum_working_set_size": int(basic.MaximumWorkingSetSize),
        "active_process_limit": int(basic.ActiveProcessLimit),
        "affinity": int(basic.Affinity),
        "priority_class": int(basic.PriorityClass),
        "scheduling_class": int(basic.SchedulingClass),
        "process_memory_limit": int(info.ProcessMemoryLimit),
        "job_memory_limit": int(info.JobMemoryLimit),
        "peak_process_memory": int(info.PeakProcessMemoryUsed),
        "peak_job_memory": int(info.PeakJobMemoryUsed),
        "returned_bytes": int(returned.value),
    }
    expected_flags = JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE | JOB_OBJECT_LIMIT_ACTIVE_PROCESS
    if result["returned_bytes"] != ctypes.sizeof(info):
        raise StageCError(f"Job limit receipt size mismatch: {result!r}")
    if result["limit_flags"] != expected_flags:
        raise StageCError(f"Job limit flags are not exact: {result!r}")
    if result["active_process_limit"] != 1:
        raise StageCError(f"Job active-process limit is not exactly one: {result!r}")
    zero_fields = (
        "per_process_user_time_limit",
        "per_job_user_time_limit",
        "minimum_working_set_size",
        "maximum_working_set_size",
        "affinity",
        "priority_class",
        "scheduling_class",
        "process_memory_limit",
        "job_memory_limit",
    )
    if any(result[name] != 0 for name in zero_fields):
        raise StageCError(f"unexpected Job limit is configured: {result!r}")
    return result


def _process_command_line(handle: wt.HANDLE) -> str:
    required = wt.ULONG()
    ntdll.NtQueryInformationProcess(
        handle,
        PROCESS_COMMAND_LINE_INFORMATION,
        None,
        0,
        ctypes.byref(required),
    )
    if required.value < ctypes.sizeof(UNICODE_STRING):
        raise StageCError("NtQueryInformationProcess returned no command-line size")
    storage = ctypes.create_string_buffer(required.value)
    returned = wt.ULONG()
    status = ntdll.NtQueryInformationProcess(
        handle,
        PROCESS_COMMAND_LINE_INFORMATION,
        storage,
        len(storage),
        ctypes.byref(returned),
    )
    if status != 0:
        raise StageCError(f"NtQueryInformationProcess(command line) failed: 0x{status & 0xFFFFFFFF:08X}")
    value = UNICODE_STRING.from_buffer(storage)
    if value.Length % ctypes.sizeof(ctypes.c_wchar) or value.Length > value.MaximumLength:
        raise StageCError("invalid process command-line UNICODE_STRING")
    pointer = ctypes.c_void_p.from_buffer(storage, UNICODE_STRING.Buffer.offset).value
    if pointer is None and value.Length:
        raise StageCError("process command-line buffer is null")
    return ctypes.wstring_at(pointer, value.Length // ctypes.sizeof(ctypes.c_wchar)) if value.Length else ""


def _same_file_identity(left: dict[str, Any], right: dict[str, Any]) -> bool:
    fields = ("volume_serial_64", "file_id_128", "bytes", "sha256")
    return all(left.get(field) == right.get(field) for field in fields)


def _job_pids(handle: wt.HANDLE, capacity: int = 8) -> list[int]:
    header_size = ctypes.sizeof(wt.DWORD) * 2
    storage = ctypes.create_string_buffer(header_size + ctypes.sizeof(ULONG_PTR) * capacity)
    returned = wt.DWORD()
    if not kernel32.QueryInformationJobObject(
        handle,
        JOB_OBJECT_BASIC_PROCESS_ID_LIST,
        storage,
        len(storage),
        ctypes.byref(returned),
    ):
        raise _win_error("QueryInformationJobObject(process-list)")
    assigned = ctypes.cast(storage, ctypes.POINTER(wt.DWORD))[0]
    count = ctypes.cast(storage, ctypes.POINTER(wt.DWORD))[1]
    if count > capacity or assigned < count:
        raise StageCError(f"invalid Job PID list counts: assigned={assigned}, listed={count}")
    base = ctypes.addressof(storage) + header_size
    values = ctypes.cast(base, ctypes.POINTER(ULONG_PTR))
    return [int(values[index]) for index in range(int(count))]


def _command_line(argv: Sequence[str]) -> str:
    if not argv or _norm(argv[0]) != _norm(WSL_PATH):
        raise StageCError("invalid WSL argv executable")
    for argument in argv[1:]:
        if not re.fullmatch(r"--[a-z]+", argument):
            raise StageCError(f"invalid WSL literal argument: {argument!r}")
    return '"' + argv[0] + '"' + "".join(" " + argument for argument in argv[1:])


def _child_environment() -> tuple[ctypes.Array[Any], dict[str, Any]]:
    forbidden = ("PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP", "PYTHONINSPECT")
    for key in forbidden:
        if os.environ.get(key):
            raise StageCError(f"forbidden code-loading environment variable is set: {key}")
    allowed = (
        "SystemRoot",
        "WINDIR",
        "ComSpec",
        "TEMP",
        "TMP",
        "USERPROFILE",
        "LOCALAPPDATA",
        "APPDATA",
        "ProgramData",
        "ProgramFiles",
        "ProgramFiles(x86)",
        "PROCESSOR_ARCHITECTURE",
        "PROCESSOR_IDENTIFIER",
        "NUMBER_OF_PROCESSORS",
        "OS",
    )
    values = {key: os.environ[key] for key in allowed if key in os.environ}
    values["PYTHONDONTWRITEBYTECODE"] = "1"
    values["PYTHONNOUSERSITE"] = "1"
    entries = [f"{key}={values[key]}" for key in sorted(values, key=str.casefold)]
    block_text = "\0".join(entries) + "\0\0"
    block = ctypes.create_unicode_buffer(block_text)
    return block, {
        "keys": sorted(values, key=str.casefold),
        "utf16le_sha256": _sha256_bytes(block_text.encode("utf-16le")),
    }


def _promote_stream(partial: str, final: str) -> dict[str, Any]:
    if os.path.lexists(final):
        raise StageCError(f"stream final already exists: {final}")
    if not kernel32.MoveFileExW(partial, final, MOVEFILE_WRITE_THROUGH):
        raise _win_error(f"MoveFileExW({partial}, {final})")
    try:
        size, digest = _sha256_file(final)
    except BaseException as exc:
        raise _ReceiptRegistrationLost(
            phase="stream_promotion",
            promoted_receipt={
                "path": final,
                "bytes": os.path.getsize(final) if os.path.isfile(final) else None,
                "sha256": None,
            },
            prior_receipt=(
                None
                if _ACTIVE_GLOBAL_RECEIPT_CHAIN is None
                or _ACTIVE_GLOBAL_RECEIPT_CHAIN.head is None
                else _receipt_ref(_ACTIVE_GLOBAL_RECEIPT_CHAIN.head)
            ),
            cause=exc,
            containment=None,
        ) from exc
    record = {"path": final, "bytes": size, "sha256": digest}
    chain = _ACTIVE_GLOBAL_RECEIPT_CHAIN
    if chain is not None:
        chain.register(
            record,
            {
                "schema": "anysolver.no_numba_residual.provider_stage_c_stream/1",
                "phase": "stream_promotion",
                "path": final,
                "predecessor": (
                    None if chain.head is None else _receipt_ref(chain.head)
                ),
            },
        )
    return record


def _safe_path_evidence(path: str, *, include_hash: bool) -> dict[str, Any]:
    try:
        if not os.path.lexists(path):
            return {"path": path, "exists": False}
        return _path_state(path, include_hash=include_hash)
    except BaseException as exc:
        return {
            "path": path,
            "exists": os.path.lexists(path),
            "evidence_limited": f"{type(exc).__name__}: {exc}",
        }


def _contain_failed_child(
    job: wt.HANDLE | None,
    process_info: PROCESS_INFORMATION,
    state: dict[str, Any],
) -> wt.HANDLE | None:
    """Contain and reap while retaining the process handle as the proof anchor."""
    if not process_info.hProcess:
        state["zero_pid_proven_at_failure"] = True
        state["containment_mode"] = "no_process_created"
        return job

    exit_code = wt.DWORD()
    exit_read = bool(
        kernel32.GetExitCodeProcess(process_info.hProcess, ctypes.byref(exit_code))
    )
    active = not exit_read or exit_code.value == STILL_ACTIVE
    state["exit_code_read_at_failure"] = exit_read
    if exit_read:
        state["exit_code_at_failure_before_containment"] = int(exit_code.value)

    if active:
        if not job:
            raise StageCError("active child has no retained Job handle")
        if state["termination_calls"] == 0:
            state["termination_calls"] = 1
            state["termination_reason"] = (
                "timeout" if state.get("timed_out") else "handled_exception"
            )
            terminated = bool(kernel32.TerminateJobObject(job, 0xE000C002))
            state["exception_terminate_job"] = terminated
            state["termination_returned"] = terminated
            if not terminated:
                state["termination_error"] = ctypes.get_last_error()
        else:
            state["second_termination_suppressed"] = True

        if state.get("termination_returned") is False:
            # Closing the sole Job handle invokes KILL_ON_JOB_CLOSE. This is not
            # a second TerminateJobObject call and is used only after its failure.
            if not kernel32.CloseHandle(job):
                raise _win_error("CloseHandle(Job kill-on-close containment)")
            job = None
            state["job_closed_for_kill_on_close"] = True
            state["containment_mode"] = "kill_on_job_close_after_terminate_failure"
        else:
            state["containment_mode"] = "terminate_job_object_once"

        wait_result = kernel32.WaitForSingleObject(process_info.hProcess, 30000)
        state["exception_wait_result"] = int(wait_result)
        state["termination_wait_proven"] = wait_result == WAIT_OBJECT_0
        if wait_result != WAIT_OBJECT_0:
            if job:
                if not kernel32.CloseHandle(job):
                    raise _win_error("CloseHandle(Job after nonterminal terminate wait)")
                job = None
                state["job_closed_for_kill_on_close"] = True
                state["containment_mode"] = (
                    "terminate_job_once_then_kill_on_job_close"
                )
            fallback_wait = kernel32.WaitForSingleObject(
                process_info.hProcess, 30000
            )
            state["kill_on_close_wait_result"] = int(fallback_wait)
            state["termination_wait_proven"] = fallback_wait == WAIT_OBJECT_0
            if fallback_wait != WAIT_OBJECT_0:
                state["direct_process_termination_calls"] = 1
                direct_terminated = bool(
                    kernel32.TerminateProcess(process_info.hProcess, 0xE000C003)
                )
                state["direct_process_termination_returned"] = direct_terminated
                if not direct_terminated:
                    state["direct_process_termination_error"] = ctypes.get_last_error()
                    state["retain_process_handle_on_unproven_containment"] = True
                    raise _win_error("TerminateProcess(final containment)")
                direct_wait = kernel32.WaitForSingleObject(
                    process_info.hProcess, 30000
                )
                state["direct_process_terminal_wait_result"] = int(direct_wait)
                if direct_wait != WAIT_OBJECT_0:
                    state["retain_process_handle_on_unproven_containment"] = True
                    raise StageCError(
                        "directly terminated child did not reach terminal state"
                    )
                state["termination_wait_proven"] = True
                state["containment_mode"] = (
                    "terminate_job_then_kill_on_close_then_terminate_process"
                )

    final_exit = wt.DWORD()
    if not kernel32.GetExitCodeProcess(process_info.hProcess, ctypes.byref(final_exit)):
        raise _win_error("GetExitCodeProcess(failure final)")
    state["exit_code_at_failure"] = int(final_exit.value)
    if final_exit.value == STILL_ACTIVE:
        raise StageCError("child remains active after failure containment")

    if job:
        pids = _job_pids(job)
        state["job_pids_at_failure"] = pids
        state["zero_pid_proven_at_failure"] = not pids
    else:
        state["terminal_process_handle_proof"] = True
        state["single_process_job_contract"] = True
        state["zero_pid_proven_at_failure"] = True
    if not state["zero_pid_proven_at_failure"]:
        raise StageCError("failure containment did not prove child PID absence")
    return job


def _run_contained_wsl_v4(
    check_id: str,
    argv: Sequence[str],
    timeout_seconds: int,
    check_dir: str,
    common: dict[str, Any],
    predecessor: dict[str, Any],
    *,
    run_id: str,
) -> dict[str, Any]:
    start_ns = time.monotonic_ns()
    job: wt.HANDLE | None = None
    process_info = PROCESS_INFORMATION()
    process_created = False
    process_resumed = False
    attribute_initialized = False
    attribute_buffer: ctypes.Array[Any] | None = None
    stdin_handle: wt.HANDLE | None = None
    stdout_fd: int | None = None
    stderr_fd: int | None = None
    stdout_handle = 0
    stderr_handle = 0
    stdout_partial = os.path.join(check_dir, "stdout.bin.partial")
    stderr_partial = os.path.join(check_dir, "stderr.bin.partial")
    stdout_final = os.path.join(check_dir, "stdout.bin")
    stderr_final = os.path.join(check_dir, "stderr.bin")
    state: dict[str, Any] = {
        "check_id": check_id,
        "run_id": run_id,
        "argv": list(argv),
        "argv_sha256": _sha256_bytes(_canonical_json(list(argv))),
        "timeout_seconds": timeout_seconds,
        "started_utc": _utc(),
        "process_created": False,
        "process_resumed": False,
        "timed_out": False,
        "termination_calls": 0,
    }
    wsl_identity_before_creation = _campaign_wsl_identity()
    if (
        not wsl_identity_before_creation.get("exists")
        or wsl_identity_before_creation.get("directory")
        or wsl_identity_before_creation.get("reparse")
    ):
        raise StageCError("registered wsl.exe identity is not a direct file")
    state["wsl_identity_before_creation"] = wsl_identity_before_creation
    last_receipt = predecessor
    job_intent_record = _atomic_json(
        os.path.join(check_dir, "job_intent.json"),
        {
            "schema": SCHEMA_JOB,
            **common,
            **state,
            "phase": "intent",
            "predecessor": _receipt_ref(last_receipt),
        },
    )
    last_receipt = job_intent_record
    attributes_intent_record = _atomic_json(
        os.path.join(check_dir, "creation_attributes_intent.json"),
        {
            "schema": SCHEMA_ATTRIBUTES,
            **common,
            **state,
            "phase": "intent",
            "predecessor": _receipt_ref(last_receipt),
            "handle_list_attribute": PROC_THREAD_ATTRIBUTE_HANDLE_LIST,
            "job_list_attribute": PROC_THREAD_ATTRIBUTE_JOB_LIST,
        },
    )
    last_receipt = attributes_intent_record
    try:
        job = kernel32.CreateJobObjectW(None, None)
        if not job:
            raise _win_error("CreateJobObjectW")
        _set_handle_inheritable(job, False)
        limits = JOBOBJECT_EXTENDED_LIMIT_INFORMATION()
        limits.BasicLimitInformation.LimitFlags = (
            JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE | JOB_OBJECT_LIMIT_ACTIVE_PROCESS
        )
        limits.BasicLimitInformation.ActiveProcessLimit = 1
        if not kernel32.SetInformationJobObject(
            job,
            JOB_OBJECT_EXTENDED_LIMIT_INFORMATION,
            ctypes.byref(limits),
            ctypes.sizeof(limits),
        ):
            raise _win_error("SetInformationJobObject")
        limit_readback = _job_limits(job)
        expected_flags = JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE | JOB_OBJECT_LIMIT_ACTIVE_PROCESS
        if (
            limit_readback["limit_flags"] & expected_flags != expected_flags
            or limit_readback["active_process_limit"] != 1
        ):
            raise StageCError(f"Job limit read-back mismatch: {limit_readback!r}")
        job_configured_record = _atomic_json(
            os.path.join(check_dir, "job_configured.json"),
            {
                "schema": SCHEMA_JOB,
                **common,
                **state,
                "phase": "configured",
                "predecessor": _receipt_ref(last_receipt),
                "job_handle": _handle_int(job),
                "job_handle_inheritable": _handle_inheritable(job),
                "job_limits": limit_readback,
                "job_pids": _job_pids(job),
            },
        )
        last_receipt = job_configured_record

        if os.path.lexists(stdout_partial) or os.path.lexists(stderr_partial):
            raise StageCError("raw stream partial already exists")
        file_flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_BINARY
        stdout_fd = os.open(stdout_partial, file_flags, 0o600)
        stderr_fd = os.open(stderr_partial, file_flags, 0o600)
        stdout_handle = msvcrt.get_osfhandle(stdout_fd)
        stderr_handle = msvcrt.get_osfhandle(stderr_fd)
        _set_handle_inheritable(stdout_handle, True)
        _set_handle_inheritable(stderr_handle, True)
        inheritable_sa = SECURITY_ATTRIBUTES()
        inheritable_sa.nLength = ctypes.sizeof(inheritable_sa)
        inheritable_sa.bInheritHandle = True
        stdin_handle = kernel32.CreateFileW(
            "NUL",
            GENERIC_READ,
            FILE_SHARE_READ | FILE_SHARE_WRITE,
            ctypes.byref(inheritable_sa),
            OPEN_EXISTING,
            0,
            None,
        )
        if _handle_int(stdin_handle) == INVALID_HANDLE_VALUE:
            raise _win_error("CreateFileW(NUL)")
        _set_handle_inheritable(stdin_handle, True)
        if _handle_inheritable(job):
            raise StageCError("Job handle unexpectedly inheritable")

        attribute_size = SIZE_T()
        first = kernel32.InitializeProcThreadAttributeList(
            None, 2, 0, ctypes.byref(attribute_size)
        )
        first_error = ctypes.get_last_error()
        if first or first_error != ERROR_INSUFFICIENT_BUFFER or not attribute_size.value:
            raise StageCError(
                "InitializeProcThreadAttributeList size probe did not return "
                f"ERROR_INSUFFICIENT_BUFFER: ok={bool(first)} error={first_error} "
                f"size={attribute_size.value}"
            )
        attribute_buffer = ctypes.create_string_buffer(attribute_size.value)
        attribute_pointer = ctypes.cast(attribute_buffer, wt.LPVOID)
        if not kernel32.InitializeProcThreadAttributeList(
            attribute_pointer, 2, 0, ctypes.byref(attribute_size)
        ):
            raise _win_error("InitializeProcThreadAttributeList")
        attribute_initialized = True
        handle_array = (wt.HANDLE * 3)(
            wt.HANDLE(_handle_int(stdin_handle)),
            wt.HANDLE(stdout_handle),
            wt.HANDLE(stderr_handle),
        )
        job_array = (wt.HANDLE * 1)(wt.HANDLE(_handle_int(job)))
        if not kernel32.UpdateProcThreadAttribute(
            attribute_pointer,
            0,
            PROC_THREAD_ATTRIBUTE_HANDLE_LIST,
            ctypes.cast(handle_array, wt.LPVOID),
            ctypes.sizeof(handle_array),
            None,
            None,
        ):
            raise _win_error("UpdateProcThreadAttribute(HANDLE_LIST)")
        if not kernel32.UpdateProcThreadAttribute(
            attribute_pointer,
            0,
            PROC_THREAD_ATTRIBUTE_JOB_LIST,
            ctypes.cast(job_array, wt.LPVOID),
            ctypes.sizeof(job_array),
            None,
            None,
        ):
            raise _win_error("UpdateProcThreadAttribute(JOB_LIST)")

        startup = STARTUPINFOEXW()
        startup.StartupInfo.cb = ctypes.sizeof(startup)
        startup.StartupInfo.dwFlags = STARTF_USESTDHANDLES
        startup.StartupInfo.hStdInput = wt.HANDLE(_handle_int(stdin_handle))
        startup.StartupInfo.hStdOutput = wt.HANDLE(stdout_handle)
        startup.StartupInfo.hStdError = wt.HANDLE(stderr_handle)
        startup.lpAttributeList = attribute_pointer
        command_line = _command_line(argv)
        command_buffer = ctypes.create_unicode_buffer(command_line)
        environment_buffer, environment_record = _child_environment()
        ready = {
            "schema": SCHEMA_ATTRIBUTES,
            **common,
            **state,
            "phase": "creation_attributes_ready",
            "predecessor": _receipt_ref(last_receipt),
            "job_handle": _handle_int(job),
            "job_handle_inheritable": _handle_inheritable(job),
            "job_limits": limit_readback,
            "attribute_capacity": 2,
            "attribute_bytes": int(attribute_size.value),
            "handle_list_attribute": PROC_THREAD_ATTRIBUTE_HANDLE_LIST,
            "job_list_attribute": PROC_THREAD_ATTRIBUTE_JOB_LIST,
            "handle_list": [
                _handle_int(stdin_handle),
                stdout_handle,
                stderr_handle,
            ],
            "handle_inheritance": {
                "stdin": _handle_inheritable(stdin_handle),
                "stdout": _handle_inheritable(stdout_handle),
                "stderr": _handle_inheritable(stderr_handle),
                "job": _handle_inheritable(job),
            },
            "startup_flags": STARTF_USESTDHANDLES,
            "creation_flags": (
                CREATE_SUSPENDED
                | EXTENDED_STARTUPINFO_PRESENT
                | CREATE_UNICODE_ENVIRONMENT
                | CREATE_NEW_PROCESS_GROUP
            ),
            "command_line_sha256": _sha256_bytes(command_line.encode("utf-16le")),
            "environment": environment_record,
            "utc": _utc(),
        }
        ready_record = _atomic_json(
            os.path.join(check_dir, "creation_attributes_ready.json"), ready
        )
        last_receipt = ready_record

        creation_flags = (
            CREATE_SUSPENDED
            | EXTENDED_STARTUPINFO_PRESENT
            | CREATE_UNICODE_ENVIRONMENT
            | CREATE_NEW_PROCESS_GROUP
        )
        if not kernel32.CreateProcessW(
            WSL_PATH,
            command_buffer,
            None,
            None,
            True,
            creation_flags,
            ctypes.cast(environment_buffer, wt.LPVOID),
            WORKDIR,
            ctypes.cast(ctypes.byref(startup), ctypes.POINTER(STARTUPINFOW)),
            ctypes.byref(process_info),
        ):
            raise _win_error("CreateProcessW(wsl.exe)")
        process_created = True
        state["process_created"] = True
        _set_handle_inheritable(stdin_handle, False)
        _set_handle_inheritable(stdout_handle, False)
        _set_handle_inheritable(stderr_handle, False)
        pids = _job_pids(job)
        if pids != [int(process_info.dwProcessId)]:
            raise StageCError(
                f"creation-time Job membership mismatch: {pids!r} != "
                f"[{process_info.dwProcessId}]"
            )
        image, image_error, process_start = _process_image(int(process_info.dwProcessId))
        if image_error is not None or image is None or _norm(image) != _norm(WSL_PATH):
            raise StageCError(
                f"created process image mismatch: image={image!r} error={image_error}"
            )
        created_image_identity = _path_state(image, include_hash=True)
        observed_command_line = _process_command_line(process_info.hProcess)
        if _norm(image) != _norm(WSL_PATH):
            raise StageCError(
                "suspended child image path differs from registered wsl.exe path"
            )
        if not _same_file_identity(
            wsl_identity_before_creation, created_image_identity
        ):
            raise StageCError(
                "suspended child image file identity differs from registered wsl.exe"
            )
        if observed_command_line != command_line:
            raise StageCError(
                "suspended child command line differs from exact CreateProcessW command"
            )
        assigned = {
            "schema": SCHEMA_ATTRIBUTES,
            **common,
            **state,
            "phase": "assigned_at_creation_before_resume",
            "predecessor": _receipt_ref(last_receipt),
            "pid": int(process_info.dwProcessId),
            "tid": int(process_info.dwThreadId),
            "image": image,
            "image_identity": created_image_identity,
            "registered_wsl_identity": wsl_identity_before_creation,
            "command_line_expected": command_line,
            "command_line_observed": observed_command_line,
            "command_line_exact": True,
            "image_path_exact": True,
            "image_file_identity_exact": True,
            "process_start_filetime": process_start,
            "job_pids": pids,
            "job_limits": _job_limits(job),
            "parent_handle_inheritance": {
                "stdin": _handle_inheritable(stdin_handle),
                "stdout": _handle_inheritable(stdout_handle),
                "stderr": _handle_inheritable(stderr_handle),
                "job": _handle_inheritable(job),
            },
            "utc": _utc(),
        }
        assigned_record = _atomic_json(
            os.path.join(check_dir, "assigned_at_creation_before_resume.json"), assigned
        )
        last_receipt = assigned_record
        previous_suspend = kernel32.ResumeThread(process_info.hThread)
        if previous_suspend == 0xFFFFFFFF or previous_suspend != 1:
            raise _win_error("ResumeThread")
        process_resumed = True
        state["process_resumed"] = True
        state["resume_previous_count"] = int(previous_suspend)
        wait_started_ns = time.monotonic_ns()
        resource_observations = 0
        peak_combined_working_set = 0
        peak_combined_conservative = 0
        last_combined_resource: dict[str, Any] | None = None
        wait_result = WAIT_TIMEOUT
        while wait_result == WAIT_TIMEOUT:
            wait_result = kernel32.WaitForSingleObject(process_info.hProcess, 100)
            if wait_result not in (WAIT_TIMEOUT, WAIT_OBJECT_0):
                raise StageCError(f"unexpected WaitForSingleObject result: {wait_result}")
            if wait_result == WAIT_TIMEOUT:
                last_combined_resource = _combined_resource_snapshot(
                    job, process_info.hProcess
                )
                resource_observations += 1
                peak_combined_working_set = max(
                    peak_combined_working_set,
                    int(last_combined_resource["combined_working_set_bytes"]),
                )
                peak_combined_conservative = max(
                    peak_combined_conservative,
                    int(last_combined_resource["combined_conservative_peak_bytes"]),
                )
                _deadline_guard(int(common["campaign_started_monotonic_ns"]))
                semantic_elapsed_ms = (
                    time.monotonic_ns() - wait_started_ns
                ) // 1_000_000
                if semantic_elapsed_ms >= timeout_seconds * 1000:
                    state["timed_out"] = True
                    state["semantic_timeout_started_after_resume"] = True
                    wait_result = WAIT_TIMEOUT
                    break
        state["combined_resource_observation_count"] = resource_observations
        state["combined_peak_working_set_bytes"] = peak_combined_working_set
        state["combined_conservative_peak_bytes"] = peak_combined_conservative
        state["combined_resource_last"] = last_combined_resource
        state["wait_result"] = int(wait_result)
        state["wait_milliseconds"] = (time.monotonic_ns() - wait_started_ns) // 1_000_000
        if wait_result == WAIT_TIMEOUT:
            state["timed_out"] = True
            if state["termination_calls"] != 0:
                raise StageCError("timeout termination was already attempted")
            state["termination_calls"] = 1
            timeout_terminated = bool(kernel32.TerminateJobObject(job, 0xE000C001))
            state["termination_returned"] = timeout_terminated
            if not timeout_terminated:
                raise _win_error("TerminateJobObject(timeout)")
            state["termination_reason"] = "timeout"
            state["termination_returned"] = True
            terminal_wait = kernel32.WaitForSingleObject(process_info.hProcess, 30000)
            state["timeout_terminal_wait"] = int(terminal_wait)
            if terminal_wait != WAIT_OBJECT_0:
                raise StageCError("timed-out Job child did not reach terminal state")
            timeout_exit = wt.DWORD()
            if not kernel32.GetExitCodeProcess(
                process_info.hProcess, ctypes.byref(timeout_exit)
            ):
                raise _win_error("GetExitCodeProcess(timeout)")
            state["exit_code"] = int(timeout_exit.value)
            timeout_pids = _job_pids(job)
            state["job_pids_after_timeout"] = timeout_pids
            if timeout_pids:
                raise StageCError(
                    f"timed-out Job retains process IDs after wait: {timeout_pids!r}"
                )
            state["timeout_zero_pid_proven"] = True
            raise StageCError(f"{check_id} timed out")
        elif wait_result != WAIT_OBJECT_0:
            raise StageCError(f"unexpected WaitForSingleObject result: {wait_result}")

        terminal_resource = _combined_resource_snapshot(job, process_info.hProcess)
        state["combined_resource_terminal"] = terminal_resource
        state["combined_resource_observation_count"] += 1
        state["combined_peak_working_set_bytes"] = max(
            int(state["combined_peak_working_set_bytes"]),
            int(terminal_resource["combined_working_set_bytes"]),
        )
        state["combined_conservative_peak_bytes"] = max(
            int(state["combined_conservative_peak_bytes"]),
            int(terminal_resource["combined_conservative_peak_bytes"]),
        )
        exit_code = wt.DWORD()
        if not kernel32.GetExitCodeProcess(process_info.hProcess, ctypes.byref(exit_code)):
            raise _win_error("GetExitCodeProcess")
        if exit_code.value == STILL_ACTIVE:
            raise StageCError("child remains active after terminal wait")
        state["exit_code"] = int(exit_code.value)
        if _job_pids(job):
            raise StageCError(f"Job retains active process IDs after wait: {_job_pids(job)!r}")
        state["job_final"] = _job_limits(job)

        if stdout_fd is not None:
            os.fsync(stdout_fd)
            os.close(stdout_fd)
            stdout_fd = None
        if stderr_fd is not None:
            os.fsync(stderr_fd)
            os.close(stderr_fd)
            stderr_fd = None
        _close_handle(stdin_handle)
        stdin_handle = None
        stdout_record = _promote_stream(stdout_partial, stdout_final)
        stderr_record = _promote_stream(stderr_partial, stderr_final)
        _close_handle(process_info.hThread)
        process_info.hThread = None
        _close_handle(process_info.hProcess)
        process_info.hProcess = None
        if attribute_initialized:
            kernel32.DeleteProcThreadAttributeList(attribute_pointer)
            attribute_initialized = False
        _close_handle(job)
        job = None
        state["finished_utc"] = _utc()
        state["wall_milliseconds"] = (time.monotonic_ns() - start_ns) // 1_000_000
        state["stdout"] = stdout_record
        state["stderr"] = stderr_record
        state["zero_job_processes"] = True
        state["handles_closed"] = True
        creation_final_record = _atomic_json(
            os.path.join(check_dir, "creation_attributes_final.json"),
            {
                "schema": SCHEMA_ATTRIBUTES,
                **common,
                **state,
                "phase": "final",
                "predecessor": _receipt_ref(last_receipt),
            },
        )
        last_receipt = creation_final_record
        process_record = _atomic_json(
            os.path.join(check_dir, "process.json"),
            {
                "schema": SCHEMA_PROCESS,
                **common,
                **state,
                "phase": "normal_terminal",
                "predecessor": _receipt_ref(last_receipt),
            },
        )
        last_receipt = process_record
        job_process_record = _atomic_json(
            os.path.join(check_dir, "job_process.json"),
            {
                "schema": SCHEMA_JOB,
                **common,
                **state,
                "phase": "normal_terminal",
                "predecessor": _receipt_ref(last_receipt),
            },
        )
        last_receipt = job_process_record
        with open(stdout_final, "rb") as stream:
            stdout = stream.read()
        with open(stderr_final, "rb") as stream:
            stderr = stream.read()
        return {
            **state,
            "stdout_bytes": stdout,
            "stderr_bytes": stderr,
            "terminal_receipt": _receipt_ref(last_receipt),
        }
    except BaseException as exc:
        original = f"{type(exc).__name__}: {exc}"
        state["failure"] = original
        state["failure_utc"] = _utc()
        try:
            if process_created:
                job = _contain_failed_child(job, process_info, state)
            else:
                state["zero_pid_proven_at_failure"] = True
                state["containment_mode"] = "creation_failed_before_process"
        except BaseException as containment_exc:
            state["containment_error"] = (
                f"{type(containment_exc).__name__}: {containment_exc}"
            )
            if state.get("job_closed_for_kill_on_close"):
                job = None
        close_evidence: dict[str, Any] = {}
        if process_info.hThread:
            close_evidence["thread_handle_closed"] = bool(
                kernel32.CloseHandle(process_info.hThread)
            )
            if not close_evidence["thread_handle_closed"]:
                close_evidence["thread_handle_close_error"] = ctypes.get_last_error()
            else:
                process_info.hThread = None
        if state.get("zero_pid_proven_at_failure") and process_info.hProcess:
            close_evidence["process_handle_closed_after_proof"] = bool(
                kernel32.CloseHandle(process_info.hProcess)
            )
            if not close_evidence["process_handle_closed_after_proof"]:
                close_evidence["process_handle_close_error"] = ctypes.get_last_error()
            else:
                process_info.hProcess = None
        elif process_info.hProcess:
            close_evidence["process_handle_retained_due_unproven_containment"] = True
        if state.get("zero_pid_proven_at_failure") and job:
            close_evidence["job_handle_closed_after_proof"] = bool(
                kernel32.CloseHandle(job)
            )
            if not close_evidence["job_handle_closed_after_proof"]:
                close_evidence["job_handle_close_error"] = ctypes.get_last_error()
            else:
                job = None
        state["handled_failure_handle_close"] = close_evidence
        for descriptor_name in ("stdout_fd", "stderr_fd"):
            descriptor = stdout_fd if descriptor_name == "stdout_fd" else stderr_fd
            if descriptor is not None:
                try:
                    os.fsync(descriptor)
                except OSError as flush_exc:
                    state[descriptor_name + "_flush_error"] = str(flush_exc)
                try:
                    os.close(descriptor)
                except OSError as close_exc:
                    state[descriptor_name + "_close_error"] = str(close_exc)
                if descriptor_name == "stdout_fd":
                    stdout_fd = None
                else:
                    stderr_fd = None
        for name, handle in (("stdin", stdin_handle),):
            try:
                if _close_handle(handle):
                    state[name + "_closed"] = True
            except BaseException as close_exc:
                state[name + "_close_error"] = str(close_exc)
        stdin_handle = None
        if attribute_initialized:
            try:
                kernel32.DeleteProcThreadAttributeList(attribute_pointer)
                state["attribute_list_deleted"] = True
            except BaseException as delete_exc:
                state["attribute_delete_error"] = str(delete_exc)
            attribute_initialized = False
        state["retained_handles_at_failure_publication"] = {
            "thread": bool(process_info.hThread),
            "process": bool(process_info.hProcess),
            "job": bool(job),
        }
        state["failure_stream_partials"] = {
            "stdout": _safe_path_evidence(stdout_partial, include_hash=True),
            "stderr": _safe_path_evidence(stderr_partial, include_hash=True),
        }
        terminal_proof: dict[str, Any] | None = None
        if bool(state.get("zero_pid_proven_at_failure")):
            terminal_proof = _v5_retain_contained_terminal_proof(
                run_id,
                state,
                owner_scope="run_contained_wsl_ordinary_failure_already_contained",
                reason="ordinary_failure_already_contained",
            )
        if isinstance(exc, (_ReceiptRegistrationLost, _ContainmentProofLost)):
            zero_pid = bool(state.get("zero_pid_proven_at_failure"))
            containment = {
                "owner": "_run_contained_wsl_v4",
                "terminal": zero_pid,
                "zero_pid": zero_pid,
                "containment_errors": (
                    []
                    if state.get("containment_error") is None
                    else [state["containment_error"]]
                ),
                "job_identity": state.get("job_handle_identity"),
                "pid": state.get("pid", int(process_info.dwProcessId or 0)),
                "process_creation_identity": state.get("process_creation_identity"),
                "handled_failure_handle_close": close_evidence,
                "retained_handles": state["retained_handles_at_failure_publication"],
                "stream_partials": state["failure_stream_partials"],
            }
            if not zero_pid:
                raise _ContainmentProofLost(
                    phase="contained_wsl_fatal",
                    run_id=run_id,
                    durable_head=(
                        None
                        if _ACTIVE_GLOBAL_RECEIPT_CHAIN is None
                        or _ACTIVE_GLOBAL_RECEIPT_CHAIN.head is None
                        else _receipt_ref(_ACTIVE_GLOBAL_RECEIPT_CHAIN.head)
                    ),
                    promoted_receipt=getattr(exc, "promoted_receipt", None),
                    cause=exc,
                    containment=containment,
                ) from exc
            if terminal_proof is not None:
                _v5_attach_retained_proof(exc, run_id)
            else:
                exc.containment = containment
                exc.run_id = run_id
            raise
        try:
            last_receipt = _route_prejob_ordinary_failure_once(
                check_dir=check_dir,
                common=common,
                state=state,
                last_receipt=last_receipt,
                prejob_failure=None,
            )
        except (_ReceiptRegistrationLost, _ContainmentProofLost) as fatal:
            fatal.containment = {
                "owner": "_run_contained_wsl_v4_failure_publisher",
                "terminal": bool(state.get("zero_pid_proven_at_failure")),
                "zero_pid": bool(state.get("zero_pid_proven_at_failure")),
                "containment_errors": (
                    []
                    if state.get("containment_error") is None
                    else [state["containment_error"]]
                ),
                "job_identity": state.get("job_handle_identity"),
                "pid": state.get("pid", int(process_info.dwProcessId or 0)),
                "process_creation_identity": state.get("process_creation_identity"),
                "handled_failure_handle_close": close_evidence,
                "retained_handles": state["retained_handles_at_failure_publication"],
            }
            if terminal_proof is not None:
                _v5_attach_retained_proof(fatal, run_id)
            else:
                fatal.run_id = run_id
            raise
        if isinstance(exc, StageCError):
            setattr(exc, "terminal_receipt", _receipt_ref(last_receipt))
            raise
        wrapped = StageCError(original)
        setattr(wrapped, "terminal_receipt", _receipt_ref(last_receipt))
        raise wrapped from exc


def _decode_wsl(raw: bytes) -> tuple[str, str]:
    if raw.startswith(b"\xff\xfe"):
        return raw.decode("utf-16"), "utf-16le-bom"
    if raw.startswith(b"\xfe\xff"):
        return raw.decode("utf-16"), "utf-16be-bom"
    if raw and len(raw) % 2 == 0 and raw[1::2].count(0) * 2 >= len(raw[1::2]):
        return raw.decode("utf-16le"), "utf-16le-heuristic"
    return raw.decode("utf-8-sig"), "utf-8"


def _semantic_check(check_id: str, process: dict[str, Any]) -> dict[str, Any]:
    stdout = process["stdout_bytes"]
    stderr = process["stderr_bytes"]
    text, encoding = _decode_wsl(stdout)
    stderr_text, stderr_encoding = _decode_wsl(stderr) if stderr else ("", "empty")
    result: dict[str, Any] = {
        "check_id": check_id,
        "exit_code": int(process["exit_code"]),
        "stdout_encoding": encoding,
        "stderr_encoding": stderr_encoding,
        "stdout_text": text,
        "stderr_text": stderr_text,
        "success": False,
    }
    if process["exit_code"] != 0:
        raise StageCError(f"{check_id} exited {process['exit_code']}: {stderr_text!r}")
    if check_id == "C02":
        match = re.search(r"(?im)^WSL version:\s*([0-9.]+)\s*$", text)
        if not match or match.group(1) != EXPECTED_WSL_VERSION:
            raise StageCError(f"C02 did not report WSL {EXPECTED_WSL_VERSION}: {text!r}")
        result["wsl_version"] = match.group(1)
    elif check_id == "C03":
        match = re.search(r"(?im)^Default Version:\s*([0-9]+)\s*$", text)
        if not match or match.group(1) != "2":
            raise StageCError(f"C03 did not report default version 2: {text!r}")
        result["default_version"] = 2
    elif check_id == "C04":
        rows = []
        for line in text.replace("\x00", "").splitlines():
            stripped = line.strip()
            if not stripped or ("NAME" in stripped and "STATE" in stripped and "VERSION" in stripped):
                continue
            if "no installed distributions" in stripped.casefold():
                continue
            match = re.fullmatch(r"\*?\s*(\S+)\s+(\S+)\s+([12])", stripped)
            if not match:
                raise StageCError(f"unparsed C04 row: {line!r}")
            rows.append(
                {"name": match.group(1), "state": match.group(2), "version": int(match.group(3))}
            )
        names = [row["name"] for row in rows]
        if len(names) != len(set(names)):
            raise StageCError(f"duplicate C04 distribution names: {names!r}")
        if BUILDER_DISTRO in names or FINAL_DISTRO in names:
            raise StageCError("registered provider distro already exists in C04")
        result["rows"] = rows
        result["names"] = names
    elif check_id == "C05":
        names = [line.strip() for line in text.replace("\x00", "").splitlines() if line.strip()]
        if len(names) != len(set(names)):
            raise StageCError(f"duplicate C05 distribution names: {names!r}")
        if BUILDER_DISTRO in names or FINAL_DISTRO in names:
            raise StageCError("registered provider distro already exists in C05")
        result["names"] = names
    else:
        raise StageCError(f"unsupported semantic check: {check_id}")
    result["success"] = True
    return result


def _activation_events(
    snapshots: Sequence[dict[str, Any]], labels: Sequence[str]
) -> dict[str, list[dict[str, Any]]]:
    service_events: list[dict[str, Any]] = []
    process_events: list[dict[str, Any]] = []
    path_events: list[dict[str, Any]] = []
    os_events: list[dict[str, Any]] = []
    query_labels = {"C02", "C03", "C04", "C05"}
    for index in range(1, len(snapshots)):
        before = {row["name"]: row for row in snapshots[index - 1]["services"]}
        after = {row["name"]: row for row in snapshots[index]["services"]}
        for name in sorted(set(before) | set(after)):
            old = before.get(name, {"exists": False, "state": None, "pid": None})
            new = after.get(name, {"exists": False, "state": None, "pid": None})
            if (old.get("exists"), old.get("state"), old.get("pid")) != (
                new.get("exists"),
                new.get("state"),
                new.get("pid"),
            ):
                transitioned_to_running = bool(
                    new.get("exists")
                    and new.get("state") == 4
                    and old.get("state") != 4
                )
                service_events.append(
                    {
                        "after_check": labels[index],
                        "service": name,
                        "before_exists": bool(old.get("exists")),
                        "before_state": old.get("state"),
                        "before_pid": old.get("pid"),
                        "after_exists": bool(new.get("exists")),
                        "after_state": new.get("state"),
                        "after_pid": new.get("pid"),
                        "transitioned_to_running": transitioned_to_running,
                        "query_triggered_candidate": bool(
                            labels[index] in query_labels and transitioned_to_running
                        ),
                        "classification": (
                            "query_temporally_associated_activation"
                            if labels[index] in query_labels and transitioned_to_running
                            else "concurrent_or_non_activation_transition"
                        ),
                    }
                )
        old_processes = {
            (str(row["name"]).casefold(), int(row["pid"])): row
            for row in snapshots[index - 1]["processes"]
        }
        new_processes = {
            (str(row["name"]).casefold(), int(row["pid"])): row
            for row in snapshots[index]["processes"]
        }
        for key in sorted(set(new_processes) - set(old_processes)):
            row = new_processes[key]
            if key[0] in {
                "wsl.exe",
                "wslservice.exe",
                "wslhost.exe",
                "wslrelay.exe",
                "vmmem.exe",
                "vmmemwsl.exe",
            }:
                process_events.append(
                    {
                        "after_check": labels[index],
                        "name": row["name"],
                        "pid": row["pid"],
                        "parent_pid": row["parent_pid"],
                        "image": row["image"],
                        "query_triggered_candidate": labels[index] in query_labels,
                        "classification": (
                            "query_temporally_associated_process_start"
                            if labels[index] in query_labels
                            else "concurrent_or_unattributed_process_start"
                        ),
                    }
                )
        before_processes = {
            int(row["pid"]): row for row in snapshots[index - 1]["processes"]
        }
        after_processes = {
            int(row["pid"]): row for row in snapshots[index]["processes"]
        }
        for removed_pid in sorted(set(before_processes) - set(after_processes)):
            removed = before_processes[removed_pid]
            process_events.append(
                {
                    "after_check": labels[index],
                    "event": "removed",
                    "pid": removed_pid,
                    "before": removed,
                    "after": None,
                    "image_file_identity": removed.get("image_file_identity"),
                    "query_triggered_candidate": False,
                    "classification": "process_removal",
                }
            )
        for retained_pid in sorted(set(before_processes) & set(after_processes)):
            before_process = before_processes[retained_pid]
            after_process = after_processes[retained_pid]
            if _canonical_json(before_process.get("image_file_identity")) != _canonical_json(
                after_process.get("image_file_identity")
            ):
                process_events.append(
                    {
                        "after_check": labels[index],
                        "event": "image_file_identity_changed",
                        "pid": retained_pid,
                        "before": before_process,
                        "after": after_process,
                        "image_file_identity": after_process.get(
                            "image_file_identity"
                        ),
                        "query_triggered_candidate": False,
                        "classification": "process_image_identity_delta",
                    }
                )
        before_paths = {
            "registered": snapshots[index - 1]["paths"],
            "wsl_file": snapshots[index - 1]["wsl_file"],
        }
        after_paths = {
            "registered": snapshots[index]["paths"],
            "wsl_file": snapshots[index]["wsl_file"],
        }
        if _canonical_json(before_paths) != _canonical_json(after_paths):
            path_events.append(
                {
                    "after_check": labels[index],
                    "before": before_paths,
                    "after": after_paths,
                    "classification": "registered_host_path_delta",
                }
            )
    os_rows = [
        (labels[index], snapshot["os_identity"])
        for index, snapshot in enumerate(snapshots)
        if snapshot.get("os_identity") is not None
    ]
    for (before_label, before_os), (after_label, after_os) in zip(os_rows, os_rows[1:]):
        if _canonical_json(before_os) != _canonical_json(after_os):
            os_events.append(
                {
                    "before_check": before_label,
                    "after_check": after_label,
                    "before": before_os,
                    "after": after_os,
                    "classification": "host_os_identity_delta",
                }
            )
    snapshots_by_label = {
        label: snapshot for label, snapshot in zip(labels, snapshots)
    }
    for event in process_events:
        if "image_file_identity" in event:
            continue
        snapshot = snapshots_by_label.get(str(event.get("after_check")))
        pid = event.get("pid")
        row = next(
            (
                candidate
                for candidate in snapshot.get("processes", [])
                if candidate.get("pid") == pid
            ),
            None,
        ) if snapshot is not None else None
        event["image_file_identity"] = (
            row.get("image_file_identity") if row is not None else None
        )
    return {
        "service": service_events,
        "process": process_events,
        "path": path_events,
        "os": os_events,
    }


def _parse_expiry(value: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise StageCError(f"invalid authority expiry: {value!r}") from exc
    if parsed.tzinfo is None:
        raise StageCError("authority expiry lacks timezone")
    return parsed.astimezone(timezone.utc)


def _receipt_bool(record: dict[str, Any], key: str) -> bool:
    value = record.get(key)
    if type(value) is not bool:
        raise StageCError(f"receipt field {key!r} must be a JSON boolean")
    return value


def _receipt_int(record: dict[str, Any], key: str, *, minimum: int = 0) -> int:
    value = record.get(key)
    if type(value) is not int or value < minimum:
        raise StageCError(f"receipt field {key!r} must be an integer >= {minimum}")
    return value


def _receipt_text(record: dict[str, Any], key: str) -> str:
    value = record.get(key)
    if type(value) is not str or not value:
        raise StageCError(f"receipt field {key!r} must be a non-empty JSON string")
    return value


def _receipt_hash(record: dict[str, Any], key: str) -> str:
    value = _receipt_text(record, key)
    if not re.fullmatch(r"[0-9A-F]{64}", value):
        raise StageCError(f"receipt field {key!r} is not an uppercase SHA-256")
    return value


def _validate_receipt_scalar_types(value: Any, path: str = "receipt") -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if type(key) is not str:
                raise StageCError(f"{path} contains a non-string JSON key")
            child = f"{path}.{key}"
            if key.endswith("sha256"):
                if type(item) is not str or not re.fullmatch(r"[0-9A-F]{64}", item):
                    raise StageCError(f"{child} must be an uppercase SHA-256 string")
            if key.endswith("_utc") and type(item) is not str:
                raise StageCError(f"{child} must be a timestamp string")
            numeric = key.endswith(
                (
                    "_bytes",
                    "_seconds",
                    "_milliseconds",
                    "_bits",
                    "_serial",
                    "_index",
                    "_count",
                    "_limit",
                )
            )
            if numeric and (type(item) is not int or item < 0):
                raise StageCError(f"{child} must be a non-negative integer")
            _validate_receipt_scalar_types(item, child)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _validate_receipt_scalar_types(item, f"{path}[{index}]")
    elif isinstance(value, (str, int, float, bool)) or value is None:
        return
    else:
        raise StageCError(f"{path} contains a non-JSON scalar type")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--packet", required=True)
    parser.add_argument("--packet-sha256", required=True)
    parser.add_argument("--executor-sha256", required=True)
    parser.add_argument("--v4-manifest", required=True)
    parser.add_argument("--v4-manifest-sha256", required=True)
    parser.add_argument("--identity-ledger", required=True)
    parser.add_argument("--identity-ledger-sha256", required=True)
    parser.add_argument("--interpreter-receipt", required=True)
    parser.add_argument("--interpreter-receipt-sha256", required=True)
    parser.add_argument("--execution-authority-receipt", required=True)
    parser.add_argument("--execution-authority-sha256", required=True)
    parser.add_argument("--perf-lease-state-receipt", required=True)
    parser.add_argument("--perf-lease-state-sha256", required=True)
    parser.add_argument("--qualification-root", required=True)
    parser.add_argument("--evidence-root", required=True)
    return parser


def _v4_attribute_names(path: str) -> list[str]:
    attributes = int(kernel32.GetFileAttributesW(path))
    if attributes == INVALID_FILE_ATTRIBUTES:
        raise _win_error(f"GetFileAttributesW({path})")
    names: list[str] = []
    if attributes & FILE_ATTRIBUTE_DIRECTORY:
        names.append("Directory")
    if attributes & FILE_ATTRIBUTE_ARCHIVE:
        names.append("Archive")
    if attributes & FILE_ATTRIBUTE_REPARSE_POINT:
        names.append("ReparsePoint")
    known = FILE_ATTRIBUTE_DIRECTORY | FILE_ATTRIBUTE_ARCHIVE | FILE_ATTRIBUTE_REPARSE_POINT
    if attributes & ~known:
        names.append(f"Other:0x{attributes & ~known:08X}")
    return names


def _v4_inventory_row(root: str, path: str) -> dict[str, Any]:
    relative = "." if _norm(path) == _norm(root) else os.path.relpath(path, root).replace("\\", "/")
    attributes = _v4_attribute_names(path)
    is_directory = "Directory" in attributes
    is_reparse = "ReparsePoint" in attributes or os.path.islink(path)
    if is_reparse:
        raise StageCError(f"immutable V4 inventory contains a link/reparse point: {path}")
    row: dict[str, Any] = {
        "relative_path": relative,
        "kind": "directory" if is_directory else "file",
        "attributes": attributes,
        "is_reparse": False,
        "is_link": False,
        "bytes": None,
        "sha256": None,
    }
    if not is_directory:
        size, digest = _sha256_file(path)
        row["bytes"] = size
        row["sha256"] = digest
    return row


def _snapshot_v4_root() -> dict[str, Any]:
    root = IMMUTABLE_V4_EVIDENCE_ROOT
    _require_direct_directory(root)
    paths = [root]
    pending = [root]
    while pending:
        directory = pending.pop()
        entries = sorted(os.scandir(directory), key=lambda entry: entry.name)
        for entry in entries:
            path = entry.path
            paths.append(path)
            if entry.is_dir(follow_symlinks=False):
                pending.append(path)
    rows = [_v4_inventory_row(root, path) for path in paths]
    rows.sort(key=lambda row: str(row["relative_path"]))
    partials = [
        row["relative_path"]
        for row in rows
        if str(row["relative_path"]).endswith(".partial")
    ]
    directory_count = sum(row["kind"] == "directory" for row in rows)
    file_count = sum(row["kind"] == "file" for row in rows)
    snapshot = {
        "immutable_root": root,
        "entries": rows,
        "entries_sha256": _sha256_bytes(_canonical_json(rows)),
        "entry_count": len(rows),
        "directory_count": directory_count,
        "file_count": file_count,
        "partials": partials,
    }
    snapshot_bytes = _canonical_json(snapshot)
    return {
        **snapshot,
        "snapshot_bytes": len(snapshot_bytes),
        "snapshot_sha256": _sha256_bytes(snapshot_bytes),
    }


def _validate_v4_manifest(manifest: Mapping[str, Any]) -> dict[str, Any]:
    expected_keys = {
        "schema",
        "producer_label",
        "producer_plan_path",
        "producer_plan_sha256",
        "created_utc",
        "immutable_root",
        "entries",
        "entries_sha256",
        "entry_count",
        "directory_count",
        "file_count",
        "partials",
        "snapshot_bytes",
        "snapshot_sha256",
        "historical_attestations",
        "identity_rows",
    }
    if set(manifest) != expected_keys:
        raise StageCError("V4 manifest top-level schema keys are not exact")
    if manifest.get("schema") != (
        "anysolver.no_numba_residual.stage_c_v4_immutable_evidence_manifest/2"
    ):
        raise StageCError("V4 manifest schema mismatch")
    if manifest.get("producer_label") != "governance_apply_patch_from_accepted_plan/1":
        raise StageCError("V4 manifest producer label mismatch")
    if _norm(str(manifest.get("producer_plan_path", ""))) != _norm(CATALOG_PLAN_PATH):
        raise StageCError("V4 manifest producer plan path mismatch")
    if str(manifest.get("producer_plan_sha256", "")).upper() != ACCEPTED_CATALOG_PLAN_SHA256:
        raise StageCError("V4 manifest producer plan SHA-256 mismatch")
    if not isinstance(manifest.get("created_utc"), str) or not manifest["created_utc"]:
        raise StageCError("V4 manifest created_utc is absent")
    if _norm(str(manifest.get("immutable_root", ""))) != _norm(IMMUTABLE_V4_EVIDENCE_ROOT):
        raise StageCError("V4 manifest root mismatch")
    inventory = manifest.get("entries")
    if not isinstance(inventory, list) or not inventory:
        raise StageCError("V4 manifest recursive_inventory is absent or empty")
    normalized_rows: list[dict[str, Any]] = []
    prior_path: str | None = None
    for ordinal, raw in enumerate(inventory):
        if not isinstance(raw, dict):
            raise StageCError(f"V4 manifest row {ordinal} is not an object")
        relative = str(raw.get("relative_path", raw.get("path", ""))).replace("\\", "/")
        kind = str(raw.get("kind", ""))
        if not relative or kind not in ("directory", "file"):
            raise StageCError(f"V4 manifest row {ordinal} path/kind is invalid")
        if prior_path is not None and relative <= prior_path:
            raise StageCError("V4 recursive inventory is not strictly ordinal-sorted")
        prior_path = relative
        attributes = raw.get("attributes")
        if attributes not in (["Directory"], ["Archive"]):
            raise StageCError(f"V4 manifest row {ordinal} attributes are not exact")
        byte_count = raw.get("bytes")
        sha256_raw = raw.get("sha256")
        if kind == "file":
            if not isinstance(byte_count, int) or byte_count < 0:
                raise StageCError(f"V4 manifest row {ordinal} bytes are invalid")
            sha256 = str(sha256_raw).upper()
            if not re.fullmatch(r"[0-9A-F]{64}", sha256):
                raise StageCError(f"V4 manifest row {ordinal} SHA-256 is invalid")
        else:
            if byte_count is not None or sha256_raw is not None:
                raise StageCError(f"V4 directory row {ordinal} has file identity")
            sha256 = None
        if raw.get("is_reparse") is not False or raw.get("is_link") is not False:
            raise StageCError(f"V4 manifest row {ordinal} is not a direct item")
        if set(raw) != {
            "relative_path",
            "kind",
            "attributes",
            "is_reparse",
            "is_link",
            "bytes",
            "sha256",
        }:
            raise StageCError(f"V4 manifest row {ordinal} schema is not exact")
        row = {
            "relative_path": relative,
            "kind": kind,
            "attributes": list(attributes),
            "is_reparse": False,
            "is_link": False,
            "bytes": byte_count,
            "sha256": sha256,
        }
        normalized_rows.append(row)
    calculated = _sha256_bytes(_canonical_json(normalized_rows))
    if str(manifest.get("entries_sha256", "")).upper() != calculated:
        raise StageCError("V4 recursive inventory digest mismatch")
    if manifest.get("partials") != []:
        raise StageCError("V4 manifest partial path list is not empty")
    if manifest.get("entry_count") != len(normalized_rows):
        raise StageCError("V4 manifest entry count mismatch")
    directory_count = sum(row["kind"] == "directory" for row in normalized_rows)
    file_count = sum(row["kind"] == "file" for row in normalized_rows)
    if manifest.get("directory_count") != directory_count:
        raise StageCError("V4 manifest directory count mismatch")
    if manifest.get("file_count") != file_count:
        raise StageCError("V4 manifest file count mismatch")
    if (
        len(normalized_rows) != 11
        or directory_count != 8
        or file_count != 3
    ):
        raise StageCError("V4 manifest exact 11/8/3 inventory counts are not satisfied")
    snapshot_payload = {
        "immutable_root": str(manifest["immutable_root"]),
        "entries": normalized_rows,
        "entries_sha256": calculated,
        "entry_count": len(normalized_rows),
        "directory_count": directory_count,
        "file_count": file_count,
        "partials": [],
    }
    snapshot_bytes = _canonical_json(snapshot_payload)
    if manifest.get("snapshot_bytes") != len(snapshot_bytes):
        raise StageCError("V4 manifest canonical snapshot byte count mismatch")
    if str(manifest.get("snapshot_sha256", "")).upper() != _sha256_bytes(snapshot_bytes):
        raise StageCError("V4 manifest canonical snapshot SHA-256 mismatch")
    raw_attestations = manifest.get("historical_attestations")
    if not isinstance(raw_attestations, list):
        raise StageCError("V4 historical attestations are not an array")
    if [
        row.get("row_id") if isinstance(row, Mapping) else None
        for row in raw_attestations
    ] != ["v4_executor", "v4_held_member"]:
        raise StageCError("V4 historical attestation labels/order are not exact")
    historical_attestations: dict[str, dict[str, Any]] = {}
    for ordinal, raw in enumerate(raw_attestations):
        if not isinstance(raw, dict) or set(raw) != {
            "row_id",
            "receipt_relative_path",
            "json_pointer",
            "path",
            "bytes",
            "sha256",
        }:
            raise StageCError(
                f"V4 historical attestation {ordinal} schema is not exact"
            )
        pointer = str(raw["json_pointer"])
        if not pointer.startswith("/") or "~" in pointer:
            raise StageCError("V4 historical attestation JSON pointer is not canonical")
        receipt_relative = str(raw["receipt_relative_path"]).replace("\\", "/")
        if receipt_relative not in {
            str(row["relative_path"])
            for row in normalized_rows
            if row["kind"] == "file"
        }:
            raise StageCError("V4 historical attestation receipt label is not a file row")
        historical_attestations[str(raw["row_id"])] = dict(raw)
    _validate_identity_rows(
        manifest.get("identity_rows"),
        expected_ids=(
            "v4_packet",
            "v4_executor",
            "v4_interpreter_receipt",
            "v4_execution_authority_receipt",
            "v4_perf_state_receipt",
            "v4_held_member",
            "v4_campaign_intent",
            "v4_preflight",
            "v4_stage_c_failure",
        ),
        expected_hashes={
            "v4_packet": "DC0E416339CCF5BB66F7EADA6C571FAEEE636129C6902D73683AEEBCBA65DA0E",
            "v4_executor": ACCEPTED_V4_EXECUTOR_SHA256,
            "v4_campaign_intent": "89384045394733BD010E1BE5B1EE4D3706C0B946C9080E1C2FC2293075D95B60",
            "v4_preflight": "F2A810CBFF4A1901F643CAEA8BC8E88724ACFB5669FFA14E1EEF7FCE1F8B141F",
            "v4_stage_c_failure": "D58E8106A46C46C250B41396A49DC3D2F612528081A59CCA8CBC25DFD8ECACEA",
        },
        historical_ids=("v4_executor", "v4_held_member"),
        historical_entries=normalized_rows,
        historical_attestations=historical_attestations,
    )
    actual = _snapshot_v4_root()
    if actual["entries"] != normalized_rows:
        raise StageCError("immutable V4 root differs from its accepted manifest")
    if actual["entries_sha256"] != calculated:
        raise StageCError("immutable V4 root digest differs from its manifest")
    for key in (
        "entry_count",
        "directory_count",
        "file_count",
        "partials",
        "snapshot_bytes",
        "snapshot_sha256",
    ):
        if actual[key] != manifest[key]:
            raise StageCError(f"immutable V4 root differs for {key}")
    return actual


def _json_pointer_get(document: Any, pointer: str) -> Any:
    current = document
    for token in pointer.split("/")[1:]:
        if isinstance(current, Mapping):
            if token not in current:
                raise StageCError(f"historical attestation pointer is absent: {pointer}")
            current = current[token]
        elif isinstance(current, list) and token.isdecimal():
            index = int(token)
            if index >= len(current):
                raise StageCError(f"historical attestation index is absent: {pointer}")
            current = current[index]
        else:
            raise StageCError(f"historical attestation pointer is invalid: {pointer}")
    return current


def _v4_receipts_attest_historical_identity(
    row: Mapping[str, Any],
    entries: Sequence[Mapping[str, Any]],
    attestation: Mapping[str, Any],
) -> bool:
    target_path = _norm(str(row["path"]))
    target_bytes = int(row["bytes"])
    target_hash = str(row["sha256"]).upper()

    if str(attestation.get("row_id")) != str(row["row_id"]):
        raise StageCError("historical attestation row label mismatch")
    if (
        _norm(str(attestation.get("path", ""))) != target_path
        or attestation.get("bytes") != target_bytes
        or str(attestation.get("sha256", "")).upper() != target_hash
    ):
        raise StageCError("historical attestation identity does not match its row")
    relative = str(attestation["receipt_relative_path"]).replace("\\", "/")
    matching = [
        entry
        for entry in entries
        if entry.get("kind") == "file" and entry.get("relative_path") == relative
    ]
    if len(matching) != 1:
        raise StageCError("historical attestation receipt label is not unique")
    receipt_path = os.path.join(
        IMMUTABLE_V4_EVIDENCE_ROOT, relative.replace("/", os.sep)
    )
    _require_direct_file(receipt_path)
    size, digest = _sha256_file(receipt_path)
    if size != matching[0].get("bytes") or digest != matching[0].get("sha256"):
        raise StageCError("immutable V4 receipt changed during historical attestation")
    try:
        with open(receipt_path, "r", encoding="utf-8-sig", newline="") as stream:
            payload = json.load(stream)
    except BaseException as exc:
        raise StageCError(
            f"immutable V4 receipt is not readable canonical JSON: {relative}"
        ) from exc
    selected = _json_pointer_get(payload, str(attestation["json_pointer"]))
    if not isinstance(selected, Mapping):
        raise StageCError("historical attestation pointer did not select an identity")
    return (
        _norm(str(selected.get("path", ""))) == target_path
        and selected.get("bytes") == target_bytes
        and str(selected.get("sha256", "")).upper() == target_hash
    )


def _validate_identity_rows(
    raw_rows: Any,
    *,
    expected_ids: Sequence[str],
    expected_paths: Mapping[str, str] | None = None,
    expected_hashes: Mapping[str, str] | None = None,
    historical_ids: Sequence[str] = (),
    historical_entries: Sequence[Mapping[str, Any]] = (),
    historical_attestations: Mapping[str, Mapping[str, Any]] | None = None,
) -> dict[str, dict[str, Any]]:
    if not isinstance(raw_rows, list):
        raise StageCError("identity rows are not an array")
    row_ids = [
        str(row.get("row_id", "")) if isinstance(row, dict) else ""
        for row in raw_rows
    ]
    if row_ids != list(expected_ids):
        raise StageCError(f"identity row order mismatch: {row_ids!r}")
    rows: dict[str, dict[str, Any]] = {}
    seen_paths: set[str] = set()
    seen_identities: set[tuple[int, str]] = set()
    historical = set(historical_ids)
    for ordinal, raw in enumerate(raw_rows):
        if not isinstance(raw, dict) or set(raw) != {"row_id", "path", "bytes", "sha256"}:
            raise StageCError(f"identity row {ordinal} schema is not exact")
        row_id = str(raw["row_id"])
        path = str(raw["path"])
        if not os.path.isabs(path) or os.path.normpath(path) != path:
            raise StageCError(f"identity row {row_id} path is not canonical absolute")
        normalized = _norm(path)
        if normalized in seen_paths:
            raise StageCError(f"identity row path is duplicated: {path}")
        seen_paths.add(normalized)
        if expected_paths is not None and row_id in expected_paths:
            if normalized != _norm(expected_paths[row_id]):
                raise StageCError(f"identity row {row_id} path mismatch")
        if not isinstance(raw["bytes"], int) or raw["bytes"] < 0:
            raise StageCError(f"identity row {row_id} byte count is invalid")
        digest = str(raw["sha256"]).upper()
        if not re.fullmatch(r"[0-9A-F]{64}", digest):
            raise StageCError(f"identity row {row_id} SHA-256 is invalid")
        if expected_hashes is not None and row_id in expected_hashes:
            if digest != str(expected_hashes[row_id]).upper():
                raise StageCError(f"identity row {row_id} accepted SHA-256 mismatch")
        identity_key = (int(raw["bytes"]), digest)
        if identity_key in seen_identities:
            raise StageCError(f"identity row {row_id} duplicates a bytes/SHA identity")
        seen_identities.add(identity_key)
        if row_id in historical:
            if historical_attestations is None or row_id not in historical_attestations:
                raise StageCError(
                    f"historical identity row {row_id} lacks a labeled attestation"
                )
            if not _v4_receipts_attest_historical_identity(
                raw,
                historical_entries,
                historical_attestations[row_id],
            ):
                raise StageCError(
                    f"historical identity row {row_id} is not attested by immutable V4 receipts"
                )
            actual_bytes, actual_hash = int(raw["bytes"]), digest
        else:
            _require_direct_file(path)
            actual_bytes, actual_hash = _sha256_file(path)
            if actual_bytes != raw["bytes"] or actual_hash != digest:
                raise StageCError(f"identity row {row_id} no longer matches its file")
        rows[row_id] = {
            "row_id": row_id,
            "path": path,
            "bytes": actual_bytes,
            "sha256": actual_hash,
        }
    return rows


def _validate_external_identity_ledger(
    ledger: Mapping[str, Any],
    *,
    packet_hash: str,
    executor_hash: str,
    manifest_hash: str,
    interpreter_receipt_path: str,
    interpreter_receipt_hash: str,
) -> dict[str, dict[str, Any]]:
    if set(ledger) != {
        "schema",
        "ledger_path",
        "created_utc",
        "acceptance_scope",
        "identity_rows",
    }:
        raise StageCError("external identity ledger top-level schema keys are not exact")
    if ledger.get("schema") != SCHEMA_IDENTITY_LEDGER:
        raise StageCError("external identity ledger schema mismatch")
    if _norm(str(ledger.get("ledger_path", ""))) != _norm(IDENTITY_LEDGER_PATH):
        raise StageCError("external identity ledger path mismatch")
    for key in ("created_utc", "acceptance_scope"):
        if not isinstance(ledger.get(key), str) or not ledger[key]:
            raise StageCError(f"external identity ledger {key} is absent")
    return _validate_identity_rows(
        ledger.get("identity_rows"),
        expected_ids=(
            "correction_plan",
            "packet_v6",
            "executor_v6",
            "focused_catalog_contract_v2",
            "v4_manifest",
            "interpreter_receipt",
        ),
        expected_paths={
            "correction_plan": CATALOG_PLAN_PATH,
            "packet_v6": PACKET_PATH,
            "executor_v6": EXECUTOR_PATH,
            "focused_catalog_contract_v2": (
                r"C:\Github\ANYopenSoft\governance\tests\test_anysolver_stage_c_catalog_c01_contract.py"
            ),
            "v4_manifest": V4_MANIFEST_PATH,
            "interpreter_receipt": interpreter_receipt_path,
        },
        expected_hashes={
            "correction_plan": ACCEPTED_CATALOG_PLAN_SHA256,
            "packet_v6": packet_hash,
            "executor_v6": executor_hash,
            "v4_manifest": manifest_hash,
            "interpreter_receipt": interpreter_receipt_hash,
        },
    )


def _preflight(args: argparse.Namespace) -> dict[str, Any]:
    if os.name != "nt" or sys.implementation.name != "cpython":
        raise StageCError("executor requires Windows CPython")
    if sys.version_info[:3] != EXPECTED_PYTHON:
        raise StageCError(f"unexpected CPython version: {sys.version_info[:3]!r}")
    if _norm(sys.executable) != _norm(INTERPRETER_PATH):
        raise StageCError(f"unexpected interpreter path: {sys.executable}")
    if not sys.flags.isolated or not sys.flags.dont_write_bytecode:
        raise StageCError("executor requires -I and -B")
    if _norm(args.packet) != _norm(PACKET_PATH):
        raise StageCError("packet path mismatch")
    if _norm(args.qualification_root) != _norm(QUALIFICATION_ROOT):
        raise StageCError("qualification root mismatch")
    if _norm(args.v4_manifest) != _norm(V4_MANIFEST_PATH):
        raise StageCError("V4 manifest path mismatch")
    if _norm(args.identity_ledger) != _norm(IDENTITY_LEDGER_PATH):
        raise StageCError("external identity ledger path mismatch")
    expected_root = os.path.join(
        QUALIFICATION_ROOT,
        "provider-stage-c-" + args.packet_sha256.lower()[:16],
    )
    if _norm(args.evidence_root) != _norm(expected_root):
        raise StageCError(f"evidence root mismatch: {args.evidence_root} != {expected_root}")
    _require_direct_file(PACKET_PATH)
    _require_direct_file(EXECUTOR_PATH)
    _require_direct_file(INTERPRETER_PATH)
    _require_direct_directory(QUALIFICATION_ROOT)
    packet_bytes, packet_hash = _sha256_file(PACKET_PATH)
    executor_bytes, executor_hash = _sha256_file(EXECUTOR_PATH)
    if packet_hash != args.packet_sha256.upper():
        raise StageCError("packet SHA-256 mismatch")
    if executor_hash != args.executor_sha256.upper():
        raise StageCError("executor SHA-256 mismatch")
    v4_manifest, v4_manifest_identity = _read_canonical_receipt(
        args.v4_manifest,
        args.v4_manifest_sha256,
        SCHEMA_V4_MANIFEST,
    )
    v4_inventory_pre = _validate_v4_manifest(v4_manifest)
    identity_ledger, identity_ledger_identity = _read_canonical_receipt(
        args.identity_ledger,
        args.identity_ledger_sha256,
        SCHEMA_IDENTITY_LEDGER,
    )
    interpreter, interpreter_identity = _read_canonical_receipt(
        args.interpreter_receipt,
        args.interpreter_receipt_sha256,
        SCHEMA_INTERPRETER,
    )
    identity_ledger_rows = _validate_external_identity_ledger(
        identity_ledger,
        packet_hash=packet_hash,
        executor_hash=executor_hash,
        manifest_hash=v4_manifest_identity["sha256"],
        interpreter_receipt_path=args.interpreter_receipt,
        interpreter_receipt_hash=interpreter_identity["sha256"],
    )
    if _norm(str(interpreter.get("path", ""))) != _norm(INTERPRETER_PATH):
        raise StageCError("interpreter receipt path mismatch")
    if interpreter.get("implementation") != "cpython" or interpreter.get("version") != "3.13.9":
        raise StageCError("interpreter receipt implementation/version mismatch")
    current_python_state = _path_state(INTERPRETER_PATH, include_hash=True)
    current_python_version = _file_version(INTERPRETER_PATH)
    current_python_bytes = int(current_python_state["bytes"])
    current_python_hash = str(current_python_state["sha256"])
    if (
        interpreter.get("bytes") != current_python_bytes
        or str(interpreter.get("sha256", "")).upper() != current_python_hash
    ):
        raise StageCError("interpreter receipt file identity mismatch")
    interpreter_requirements = {
        "volume_serial": current_python_state["volume_serial"],
        "file_index": current_python_state["file_index"],
        "reparse": False,
        "directory": False,
        "file_version": current_python_version["file_version"],
        "product_version": current_python_version["product_version"],
        "implementation": "cpython",
        "version": "3.13.9",
        "architecture": "AMD64",
        "pointer_bits": 64,
        "authenticode_valid": True,
    }
    for key, expected in interpreter_requirements.items():
        if interpreter.get(key) != expected:
            raise StageCError(
                f"interpreter receipt mismatch for {key}: "
                f"{interpreter.get(key)!r} != {expected!r}"
            )
    if interpreter.get("abi") != sys.implementation.cache_tag:
        raise StageCError("interpreter receipt ABI/cache-tag mismatch")
    if not isinstance(interpreter.get("authenticode_chain_sha256"), str) or not re.fullmatch(
        r"[0-9A-F]{64}", str(interpreter.get("authenticode_chain_sha256"))
    ):
        raise StageCError("interpreter receipt lacks accepted Authenticode chain identity")
    authority, authority_identity = _read_canonical_receipt(
        args.execution_authority_receipt,
        args.execution_authority_sha256,
        SCHEMA_AUTHORITY,
    )
    perf_state, perf_identity = _read_canonical_receipt(
        args.perf_lease_state_receipt,
        args.perf_lease_state_sha256,
        SCHEMA_PERF_STATE,
    )
    required_authority = {
        "boss_thread_id": BOSS_THREAD_ID,
        "source_commit": "82a9db28d67507c82ef15c631f582a0c3bf6740e",
        "source_tree": "00b2b20691e73a05589b797b32352f1c760a2451",
        "packet_path": PACKET_PATH,
        "packet_sha256": packet_hash,
        "executor_path": EXECUTOR_PATH,
        "executor_sha256": executor_hash,
        "v4_manifest_sha256": v4_manifest_identity["sha256"],
        "identity_ledger_sha256": identity_ledger_identity["sha256"],
        "interpreter_path": INTERPRETER_PATH,
        "interpreter_sha256": current_python_hash,
        "interpreter_receipt_sha256": interpreter_identity["sha256"],
        "evidence_root": expected_root,
        "execution_authority_kind": "short_read_only",
        "deadline_seconds": DEADLINE_SECONDS,
        "finalization_reserve_seconds": FINALIZATION_RESERVE_SECONDS,
        "max_resident_bytes": MAX_COMBINED_RESIDENT_BYTES,
        "max_children": 1,
        "network": False,
        "gpu": False,
        "retry": False,
        "cleanup": False,
        "shell": False,
    }
    for key, expected in required_authority.items():
        if authority.get(key) != expected:
            raise StageCError(
                f"execution authority mismatch for {key}: {authority.get(key)!r} != {expected!r}"
            )
    now = datetime.now(timezone.utc)
    authority_expiry = _parse_expiry(str(authority.get("expires_utc", "")))
    if authority_expiry <= now:
        raise StageCError("execution authority is expired")
    authority_checks = authority.get("checks")
    expected_checks = [
        {
            "id": check_id,
            "argv": list(check_argv),
            "argv_sha256": _sha256_bytes(_canonical_json(list(check_argv))),
            "timeout_seconds": timeout,
        }
        for check_id, check_argv, timeout in CHECKS
    ]
    if authority_checks != expected_checks:
        raise StageCError("execution authority check/argv/timeout binding mismatch")
    if not isinstance(authority.get("raw_grant_message_sha256"), str) or not re.fullmatch(
        r"[0-9A-F]{64}", str(authority.get("raw_grant_message_sha256"))
    ):
        raise StageCError("execution authority lacks raw grant message identity")
    if authority.get("sandbox_permissions") not in (
        "use_default",
        "require_escalated",
    ):
        raise StageCError("execution authority sandbox permission is invalid")
    if authority.get("prefix_rule") is not None:
        raise StageCError("Stage-C execution authority must not contain a prefix rule")
    if perf_state.get("boss_thread_id") != BOSS_THREAD_ID:
        raise StageCError("PERF-state Boss thread mismatch")
    if perf_state.get("active") is not False or perf_state.get("holder") not in (None, ""):
        raise StageCError("a competing exclusive PERF lease is active")
    perf_requirements = {
        "packet_sha256": packet_hash,
        "executor_sha256": executor_hash,
        "execution_authority_sha256": authority_identity["sha256"],
        "execution_authority_kind": "short_read_only",
        "exclusive_perf_lease_consumed": False,
    }
    for key, expected in perf_requirements.items():
        if perf_state.get(key) != expected:
            raise StageCError(
                f"PERF-state receipt mismatch for {key}: "
                f"{perf_state.get(key)!r} != {expected!r}"
            )
    observed = _parse_expiry(str(perf_state.get("observed_utc", "")))
    perf_expiry = _parse_expiry(str(perf_state.get("expires_utc", "")))
    age_seconds = int((now - observed).total_seconds())
    if observed > now or age_seconds < 0 or age_seconds > 120:
        raise StageCError(f"PERF-state receipt is not fresh: age={age_seconds}s")
    if perf_expiry <= now or perf_expiry > authority_expiry:
        raise StageCError("PERF-state validity does not cover launch authority")
    if not isinstance(perf_state.get("raw_status_message_sha256"), str) or not re.fullmatch(
        r"[0-9A-F]{64}", str(perf_state.get("raw_status_message_sha256"))
    ):
        raise StageCError("PERF-state receipt lacks raw status identity")
    grant_utc_text = _receipt_text(authority, "grant_utc")
    grant_utc = _parse_expiry(grant_utc_text)
    grant_age_seconds = (now - grant_utc).total_seconds()
    if grant_age_seconds < 0 or grant_age_seconds > 120:
        raise StageCError(
            f"execution authority is not fresh: age={grant_age_seconds!r}s"
        )
    authority_coverage_seconds = (authority_expiry - now).total_seconds()
    if authority_coverage_seconds < DEADLINE_SECONDS:
        raise StageCError(
            "execution authority does not cover the complete 300-second campaign"
        )
    activation_allowed = _receipt_bool(
        authority, "query_triggered_service_activation_allowed"
    )
    _validate_receipt_scalar_types(interpreter, "interpreter_receipt")
    _validate_receipt_scalar_types(authority, "execution_authority_receipt")
    _validate_receipt_scalar_types(perf_state, "perf_state_receipt")
    if _receipt_bool(perf_state, "active") is not False:
        raise StageCError("PERF-state receipt must state active=false")
    if perf_state.get("holder") is not None:
        raise StageCError("PERF-state holder must be JSON null")
    if _receipt_bool(perf_state, "exclusive_perf_lease_consumed") is not False:
        raise StageCError("Stage-C must not consume the exclusive PERF lease")
    _receipt_text(authority, "expires_utc")
    _receipt_text(perf_state, "observed_utc")
    _receipt_text(perf_state, "expires_utc")
    _receipt_hash(authority, "raw_grant_message_sha256")
    _receipt_hash(perf_state, "raw_status_message_sha256")
    _receipt_text(interpreter, "path")
    for key in ("bytes", "volume_serial", "file_index"):
        if key in interpreter:
            _receipt_int(interpreter, key)
    if "sha256" in interpreter:
        _receipt_hash(interpreter, "sha256")
    _registered_absence_snapshot()
    if os.path.lexists(expected_root):
        raise StageCError(f"evidence root is not fresh: {expected_root}")
    return {
        "packet": {"path": PACKET_PATH, "bytes": packet_bytes, "sha256": packet_hash},
        "executor": {"path": EXECUTOR_PATH, "bytes": executor_bytes, "sha256": executor_hash},
        "v4_manifest": v4_manifest_identity,
        "v4_inventory_pre": v4_inventory_pre,
        "identity_ledger": identity_ledger_identity,
        "identity_ledger_rows": identity_ledger_rows,
        "interpreter": interpreter_identity,
        "interpreter_fields": interpreter_requirements,
        "authority": authority_identity,
        "authority_fields": {
            "query_triggered_service_activation_allowed": activation_allowed,
            "grant_utc": grant_utc_text,
            "grant_age_seconds": grant_age_seconds,
            "full_campaign_coverage_seconds": authority_coverage_seconds,
            "expires_utc": authority["expires_utc"],
            "raw_grant_message_sha256": authority.get("raw_grant_message_sha256"),
        },
        "perf_state": perf_identity,
        "perf_state_fields": {
            "active": False,
            "holder": None,
            "exclusive_perf_lease_consumed": False,
            "observed_utc": perf_state["observed_utc"],
            "expires_utc": perf_state["expires_utc"],
            "age_seconds": age_seconds,
        },
        "evidence_root": expected_root,
    }


def _v5_existing_receipt(path: str) -> dict[str, Any] | None:
    if not os.path.isfile(path):
        return None
    size, digest = _sha256_file(path)
    return {
        "path": path,
        "bytes": size,
        "sha256": digest,
    }


def _c01_held_identity_with_receipts(
    campaign_started_ns: int,
    check_dir: str,
    common: dict[str, Any],
    predecessor: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
    global _V5_C01_RECEIPT_CONTEXT

    if _V5_C01_RECEIPT_CONTEXT is not None:
        raise StageCError("C01 receipt context is already active")
    if _ACTIVE_GLOBAL_RECEIPT_CHAIN is None or _ACTIVE_GLOBAL_RECEIPT_CHAIN.head is None:
        raise StageCError("C01 receipt context has no durable global predecessor")
    if _receipt_ref(_ACTIVE_GLOBAL_RECEIPT_CHAIN.head) != _receipt_ref(predecessor):
        raise StageCError("C01 predecessor is not the mandatory global chain head")
    receipt_directory = check_dir
    candidate_directory = os.path.join(check_dir, "catalog_candidates")
    _mkdir_new(candidate_directory)
    context: dict[str, Any] = {
        "directory": receipt_directory,
        "common": common,
        "head": predecessor,
        "head_identity": {
            **_receipt_ref(predecessor),
            "schema": predecessor.get("schema"),
            "sequence": predecessor.get("sequence"),
            "predecessor": predecessor.get("predecessor"),
        },
        "chain": [],
        "sequence": 0,
        "pending_raw_events": [],
    }
    _V5_C01_RECEIPT_CONTEXT = context
    try:
        observation = _c01_held_identity(campaign_started_ns)
        if context["pending_raw_events"]:
            raise StageCError("C01 completed with unpromoted raw event evidence")
        return observation, context["head"], list(context["chain"])
    except (_ReceiptRegistrationLost, _ContainmentProofLost):
        raise
    except BaseException as exc:
        try:
            _v5_c01_emit(
                "trust_failure",
                {
                    "error": _error_record(exc),
                    "failure_utc": _utc(),
                },
            )
        except BaseException as receipt_exc:
            if isinstance(receipt_exc, (_ReceiptRegistrationLost, _ContainmentProofLost)):
                receipt_exc.c01_pending_raw_events = list(
                    context["pending_raw_events"]
                )
                raise
            setattr(exc, "c01_failure_receipt_error", _error_record(receipt_exc))
            setattr(
                exc,
                "c01_pending_raw_events",
                list(context["pending_raw_events"]),
            )
        setattr(exc, "terminal_receipt", _receipt_ref(context["head"]))
        setattr(exc, "c01_receipt_chain", list(context["chain"]))
        raise
    finally:
        _V5_C01_RECEIPT_CONTEXT = None


def _route_prejob_ordinary_failure_once(
    *,
    check_dir: str,
    common: Mapping[str, Any],
    state: dict[str, Any],
    last_receipt: dict[str, Any],
    prejob_failure: _PreJobOrdinaryFailureContext | None,
) -> dict[str, Any]:
    """Use the established process-then-Job terminal receipt order exactly once."""

    if prejob_failure is None:
        prejob_failure = {
            "ordinary_publisher_invoked": False,
            "route_kind": "post_child_failure",
        }
    if prejob_failure.get("ordinary_publisher_invoked") is not False:
        raise StageCError("ordinary pre-Job failure publisher was invoked more than once")
    prejob_failure["ordinary_publisher_invoked"] = True
    published: list[dict[str, Any]] = []
    try:
        process_failure_record = _atomic_json(
            os.path.join(check_dir, "process_failure.json"),
            {
                "schema": SCHEMA_PROCESS,
                **common,
                **state,
                "phase": "failure",
                "predecessor": _receipt_ref(last_receipt),
            },
        )
        last_receipt = process_failure_record
        published.append(_receipt_ref(process_failure_record))
        job_failure_record = _atomic_json(
            os.path.join(check_dir, "job_process_failure.json"),
            {
                "schema": SCHEMA_JOB,
                **common,
                **state,
                "phase": "failure",
                "predecessor": _receipt_ref(last_receipt),
            },
        )
        last_receipt = job_failure_record
        published.append(_receipt_ref(job_failure_record))
    except (_ReceiptRegistrationLost, _ContainmentProofLost) as fatal:
        prejob_failure["publisher_final_count"] = len(published)
        prejob_failure["publisher_finals"] = list(published)
        prejob_failure["publisher_failure"] = _error_record(fatal)
        fatal.ordinary_prejob_failure = dict(prejob_failure)
        raise
    except BaseException as evidence_exc:
        state["failure_receipt_error"] = (
            f"{type(evidence_exc).__name__}: {evidence_exc}"
        )
        prejob_failure["publisher_final_count"] = len(published)
        prejob_failure["publisher_finals"] = list(published)
        prejob_failure["publisher_failure"] = _error_record(evidence_exc)
        partial_path = getattr(evidence_exc, "partial_path", None)
        if isinstance(partial_path, str):
            try:
                prejob_failure["publisher_partial"] = {
                    "captured": True,
                    "receipt": _v5_existing_receipt(partial_path),
                }
            except BaseException as partial_exc:
                prejob_failure["publisher_partial"] = {
                    "captured": False,
                    "error": _error_record(partial_exc),
                }
    else:
        prejob_failure["publisher_final_count"] = 2
        prejob_failure["publisher_finals"] = list(published)
        prejob_failure["publisher_failure"] = None
    return last_receipt


def _prejob_failure_context(
    *,
    exc: BaseException,
    context: Mapping[str, Any],
    failing_site: str,
    prior_head: Mapping[str, Any] | None,
    no_child_created: Mapping[str, Any],
) -> _PreJobOrdinaryFailureContext:
    prior = None
    if prior_head is not None:
        prior = {
            **_receipt_ref(dict(prior_head)),
            "schema": prior_head.get("schema"),
            "sequence": prior_head.get("sequence"),
        }
    target_path = getattr(exc, "final_path", None)
    partial_path = getattr(exc, "partial_path", None)
    proof_bytes = _canonical_json(dict(no_child_created))
    secondary = list(getattr(exc, "secondary_errors", []))
    def safe_partial_identity(path: Any) -> dict[str, Any] | None:
        if not isinstance(path, str):
            return None
        try:
            receipt = _v5_existing_receipt(path)
            return {"captured": True, "receipt": receipt}
        except BaseException as identity_exc:
            return {"captured": False, "error": _error_record(identity_exc)}

    return _PreJobOrdinaryFailureContext(
        schema="anysolver.no_numba_residual.stage_c.prejob_ordinary_failure_context/1",
        run_id=str(context["run_id"]),
        run_material_sha256=str(context["material_sha256"]),
        failing_site=failing_site,
        prior_global_head=prior,
        target_final_path=(None if target_path is None else str(target_path)),
        owned_partial_path=(None if partial_path is None else str(partial_path)),
        owned_partial=safe_partial_identity(partial_path),
        promoted=False,
        primary_phase=failing_site,
        primary_type=type(exc).__name__,
        primary_message_sha256=hashlib.sha256(str(exc).encode("utf-8")).hexdigest(),
        secondary_errors=secondary,
        no_child_created=dict(no_child_created),
        no_child_created_proof_identity={
            "bytes": len(proof_bytes),
            "sha256": hashlib.sha256(proof_bytes).hexdigest().upper(),
        },
        ordinary_publisher_invoked=False,
        publisher_final_count=0,
        publisher_finals=[],
        publisher_failure=None,
        publisher_partial=None,
        created_utc=_utc(),
    )


def _run_contained_wsl(
    check_id: str,
    argv: Sequence[str],
    timeout_seconds: int,
    check_dir: str,
    common: dict[str, Any],
    predecessor: dict[str, Any],
    *,
    receipt_chain: _GlobalReceiptChain,
    run_id: str,
    run_identity_material: Mapping[str, Any],
) -> dict[str, Any]:
    """Fatal-first envelope for the three V5 pre-Job sites.

    The V4 body retains sole ownership of Job/process containment.  Any exception
    that already carries its terminal receipt came from that body and is never
    published a second time here.
    """

    context = receipt_chain.require_contained_run(run_id)
    derived = _derive_contained_run_id(run_identity_material)
    if derived != run_id or context["material"] != dict(run_identity_material):
        raise StageCError("contained run reservation/callee identity mismatch")
    try:
        process = _run_contained_wsl_v4(
            check_id,
            argv,
            timeout_seconds,
            check_dir,
            common,
            predecessor,
            run_id=run_id,
        )
        _v5_retain_contained_terminal_proof(
            run_id,
            process,
            owner_scope="run_contained_wsl_already_terminal",
            reason="already_terminal_reaped",
        )
        process["_v5_run_context"] = context
        return process
    except (_ReceiptRegistrationLost, _ContainmentProofLost) as fatal:
        if getattr(fatal, "containment", None) is None:
            try:
                _v5_attach_retained_proof(fatal, run_id)
            except BaseException as proof_exc:
                failing_site = getattr(fatal, "failing_site", None)
                if failing_site not in ("job_intent", "creation_attributes_intent"):
                    raise _ContainmentProofLost(
                        phase="post_child_terminal_proof_unavailable",
                        run_id=run_id,
                        durable_head=(
                            None if receipt_chain.head is None else dict(receipt_chain.head)
                        ),
                        promoted_receipt=getattr(fatal, "promoted_receipt", None),
                        cause=proof_exc,
                        containment={
                            "owner": "pre_job_envelope",
                            "reason": "post_child_state_not_reclassified_as_no_child",
                            "child_created": {"status": "unknown_after_creation_attempt"},
                            "terminal": False,
                            "zero_pid": False,
                            "handles_closed": False,
                            "job_identity": {"status": "unknown_after_creation_attempt"},
                            "pid": {"status": "unknown_after_creation_attempt"},
                            "process_creation_identity": {
                                "status": "unknown_after_creation_attempt"
                            },
                            "containment_errors": [_error_record(proof_exc)],
                        },
                    ) from fatal
                fatal.run_id = run_id
                fatal.containment = {
                    "owner": "pre_job_envelope",
                    "reason": "no_child_created",
                    "child_created": False,
                    "terminal": True,
                    "zero_pid": True,
                    "handles_closed": True,
                    "job_identity": None,
                    "pid": None,
                    "process_creation_identity": None,
                    "containment_errors": [],
                }
        raise
    except BaseException as exc:
        if getattr(exc, "terminal_receipt", None) is not None:
            consumer_state = _v5_finalize_run_consumers(context, lane="failure")
            setattr(exc, "run_id", run_id)
            setattr(exc, "run_consumer_manifest", consumer_state)
            raise

        failing_site = getattr(
            exc,
            "failing_site",
            "campaign_wsl_identity",
        )
        last_receipt = (
            predecessor if receipt_chain.head is None else dict(receipt_chain.head)
        )
        no_child_created = {
            "schema": "anysolver.no_numba_residual.provider_stage_c_no_child_created/1",
            "run_id": run_id,
            "owner": "pre_job_envelope",
            "job_created": False,
            "process_created": False,
            "terminal": True,
            "zero_pid": True,
            "handles_closed": True,
            "job_identity": None,
            "pid": None,
            "process_creation_identity": None,
            "containment_errors": [],
        }
        state = {
            "check_id": check_id,
            "argv": list(argv),
            "timeout_seconds": timeout_seconds,
            "run_id": run_id,
            "failure_site": failing_site,
            "failure": _error_record(exc),
            "failure_utc": _utc(),
            "process_created": False,
            "job_created": False,
            "zero_job_processes": True,
            "no_child_created": no_child_created,
        }
        terminal_proof = _v5_retain_contained_terminal_proof(
            run_id,
            state,
            owner_scope="pre_job_no_child",
            reason="no_child_created_before_job",
        )
        no_child_created["terminal_proof"] = terminal_proof
        prejob_failure = _prejob_failure_context(
            exc=exc,
            context=context,
            failing_site=failing_site,
            prior_head=last_receipt,
            no_child_created=no_child_created,
        )
        last_receipt = _route_prejob_ordinary_failure_once(
            check_dir=check_dir,
            common=common,
            state=state,
            last_receipt=last_receipt,
            prejob_failure=prejob_failure,
        )
        consumer_state = _v5_finalize_run_consumers(
            context,
            lane="failure",
            failure_final_count=int(prejob_failure["publisher_final_count"]),
        )
        routed = _PreJobOrdinaryFailureRouted(
            f"pre-Job failure routed once at {failing_site}: {exc}"
        )
        routed.run_id = run_id
        routed.failing_site = failing_site
        routed.no_child_created = no_child_created
        routed.ordinary_prejob_failure = dict(prejob_failure)
        routed.terminal_receipt = _receipt_ref(last_receipt)
        routed.run_consumer_manifest = (
            consumer_state
        )
        raise routed from exc


def _v5_complete_contained_check(
    *,
    check_id: str,
    ordinal: int,
    process: dict[str, Any],
    run_context: dict[str, Any],
    check_dir: str,
    evidence_root: str,
    common: dict[str, Any],
) -> dict[str, Any]:
    result_record: dict[str, Any] | None = None
    snapshot_record: dict[str, Any] | None = None
    try:
        semantic = _semantic_check(check_id, process)
        result = {
            "schema": SCHEMA_CHECK,
            **common,
            "check_id": check_id,
            "ordinal": ordinal,
            "predecessor": _receipt_ref(process["terminal_receipt"]),
            "process_result_path": os.path.join(check_dir, "job_process.json"),
            "exit_code": int(process["exit_code"]),
            "stdout": process["stdout"],
            "stderr": process["stderr"],
            "semantic": semantic,
            "success": bool(semantic["success"]),
            "finished_utc": _utc(),
        }
        result_record = _atomic_json(os.path.join(check_dir, "result.json"), result)
        snapshot = _host_snapshot(
            "post_" + check_id,
            include_os=False,
            predecessor=result_record,
        )
        snapshot_record = _atomic_json(
            os.path.join(evidence_root, "snapshots", "post_" + check_id + ".json"),
            snapshot,
        )
        consumer_state = _v5_finalize_run_consumers(
            run_context,
            lane="success",
            outer_receipts=(
                ("result.json", result_record),
                ("post_snapshot.json", snapshot_record),
            ),
        )
        return {
            "result": result,
            "result_record": result_record,
            "snapshot": snapshot,
            "snapshot_record": snapshot_record,
            "consumer_state": consumer_state,
        }
    except (_ReceiptRegistrationLost, _ContainmentProofLost) as fatal:
        if getattr(fatal, "containment", None) is None:
            _v5_attach_retained_proof(fatal, str(run_context["run_id"]))
        raise
    except BaseException as exc:
        outer: list[tuple[str, Mapping[str, Any]]] = []
        if result_record is not None:
            outer.append(("result.json", result_record))
        if snapshot_record is not None:
            outer.append(("post_snapshot.json", snapshot_record))
        consumer_state = _v5_finalize_run_consumers(
            run_context,
            lane="postprocess_failure",
            outer_receipts=outer,
        )
        setattr(exc, "run_id", run_context["run_id"])
        setattr(exc, "run_consumer_manifest", consumer_state)
        raise


def _main_impl(argv: Sequence[str] | None = None) -> dict[str, Any]:
    global _ACTIVE_GLOBAL_RECEIPT_CHAIN

    if _ACTIVE_GLOBAL_RECEIPT_CHAIN is not None:
        raise StageCError("global receipt chain is already active")
    args = _parser().parse_args(argv)
    root_created = False
    common: dict[str, Any] | None = None
    last_receipt: dict[str, Any] | None = None
    current_phase = "preflight"
    started_ns = time.monotonic_ns()
    c01_receipt_chain: list[dict[str, Any]] = []
    run_context: dict[str, Any] | None = None
    try:
        preflight = _preflight(args)
        campaign_wsl_identity = _acquire_campaign_wsl_hold()
        evidence_root = str(preflight["evidence_root"])
        _mkdir_new(evidence_root)
        root_created = True
        _mkdir_new(os.path.join(evidence_root, "snapshots"))
        _mkdir_new(os.path.join(evidence_root, "checks"))
        global_receipt_directory = os.path.join(evidence_root, "global_receipts")
        _mkdir_new(global_receipt_directory)
        _ACTIVE_GLOBAL_RECEIPT_CHAIN = _GlobalReceiptChain(global_receipt_directory)
        for check_id, _, _ in CHECKS:
            _mkdir_new(os.path.join(evidence_root, "checks", check_id))
        common = {
            "packet": preflight["packet"],
            "executor": preflight["executor"],
            "v4_manifest": preflight["v4_manifest"],
            "identity_ledger": preflight["identity_ledger"],
            "interpreter": preflight["interpreter"],
            "execution_authority": preflight["authority"],
            "perf_lease_state": preflight["perf_state"],
            "campaign_held_wsl_identity": campaign_wsl_identity,
            "execution_authority_kind": "short_read_only",
            "exclusive_perf_lease_consumed": False,
            "evidence_root": evidence_root,
            "campaign_started_monotonic_ns": started_ns,
            "attempt_id": str(preflight["packet"]["sha256"])[:16].lower(),
            "v4_inventory_pre": preflight["v4_inventory_pre"],
        }
        intent = {
            "schema": SCHEMA_INTENT,
            **common,
            "source_commit": "82a9db28d67507c82ef15c631f582a0c3bf6740e",
            "source_tree": "00b2b20691e73a05589b797b32352f1c760a2451",
            "qualification_root": QUALIFICATION_ROOT,
            "workdir": WORKDIR,
            "checks": [
                {"id": check_id, "argv": list(check_argv), "timeout_seconds": timeout}
                for check_id, check_argv, timeout in CHECKS
            ],
            "deadline_seconds": DEADLINE_SECONDS,
            "finalization_reserve_seconds": FINALIZATION_RESERVE_SECONDS,
            "started_utc": _utc(),
            "pid": os.getpid(),
            "query_triggered_service_activation_allowed": preflight[
                "authority_fields"
            ]["query_triggered_service_activation_allowed"],
            "preflight": preflight,
            "predecessor": None,
        }
        intent_record = _atomic_json(
            os.path.join(evidence_root, "campaign_intent.json"), intent
        )
        last_receipt = intent_record
        common["campaign_intent"] = _receipt_ref(intent_record)

        snapshots: list[dict[str, Any]] = []
        snapshot_labels: list[str] = []
        snapshot_records: list[dict[str, Any]] = []
        check_records: dict[str, dict[str, Any]] = {}
        run_consumer_records: dict[str, dict[str, Any]] = {}
        current_phase = "snapshot-preflight"
        first_snapshot = _host_snapshot(
            "preflight", include_os=True, predecessor=last_receipt
        )
        first_snapshot_record = _atomic_json(
            os.path.join(evidence_root, "snapshots", "preflight.json"),
            first_snapshot,
        )
        if _ACTIVE_GLOBAL_RECEIPT_CHAIN is None or _ACTIVE_GLOBAL_RECEIPT_CHAIN.head is None:
            raise StageCError("preflight snapshot did not advance the global chain")
        last_receipt = dict(_ACTIVE_GLOBAL_RECEIPT_CHAIN.head)
        snapshots.append(first_snapshot)
        snapshot_labels.append("preflight")
        snapshot_records.append(first_snapshot_record)

        check_results: dict[str, dict[str, Any]] = {}
        current_phase = "C01"
        if time.monotonic_ns() - started_ns > (DEADLINE_SECONDS - 30 - FINALIZATION_RESERVE_SECONDS) * 1_000_000_000:
            raise StageCError("insufficient campaign time before C01")
        c01_observation, last_receipt, c01_receipt_chain = (
            _c01_held_identity_with_receipts(
                started_ns,
                os.path.join(evidence_root, "checks", "C01"),
                common,
                last_receipt,
            )
        )
        c01_result = {
            "schema": SCHEMA_C01_RESULT,
            "attempt_id": common["attempt_id"],
            "receipt_id": "c01:result",
            "receipt_kind": "c01_result",
            "phase": "C01",
            "created_utc": _utc(),
            "sequence": len(c01_receipt_chain) + 1,
            "producer": common["executor"],
            "authority": {
                name: common[name]
                for name in (
                    "packet",
                    "identity_ledger",
                    "v4_manifest",
                    "interpreter",
                    "execution_authority",
                    "perf_lease_state",
                )
            },
            "predecessor": c01_receipt_chain[-1],
            "outcome": "success",
            "payload": {
                "held_identity": c01_observation,
                "c01_receipt_chain": list(c01_receipt_chain),
            },
            "primary_error": None,
            "secondary_errors": [],
            "success": True,
        }
        c01_record = _atomic_json(
            os.path.join(evidence_root, "checks", "C01", "result.json"), c01_result
        )
        if _ACTIVE_GLOBAL_RECEIPT_CHAIN is None or _ACTIVE_GLOBAL_RECEIPT_CHAIN.head is None:
            raise StageCError("C01 result did not advance the global chain")
        last_receipt = dict(_ACTIVE_GLOBAL_RECEIPT_CHAIN.head)
        c01_result_identity = {
            **_receipt_ref(c01_record),
            "schema": SCHEMA_C01_RESULT,
            "sequence": c01_result["sequence"],
            "predecessor": c01_result["predecessor"],
        }
        c01_receipt_chain.append(c01_result_identity)
        check_results["C01"] = c01_result
        check_records["C01"] = c01_record
        post_c01 = _host_snapshot(
            "post_C01", include_os=False, predecessor=last_receipt
        )
        post_c01_record = _atomic_json(
            os.path.join(evidence_root, "snapshots", "post_C01.json"), post_c01
        )
        if _ACTIVE_GLOBAL_RECEIPT_CHAIN is None or _ACTIVE_GLOBAL_RECEIPT_CHAIN.head is None:
            raise StageCError("post-C01 snapshot did not advance the global chain")
        last_receipt = dict(_ACTIVE_GLOBAL_RECEIPT_CHAIN.head)
        snapshots.append(post_c01)
        snapshot_labels.append("C01")
        snapshot_records.append(post_c01_record)

        for ordinal, (check_id, check_argv, timeout) in enumerate(CHECKS[1:], start=2):
            current_phase = check_id
            elapsed_seconds = (time.monotonic_ns() - started_ns) // 1_000_000_000
            if DEADLINE_SECONDS - elapsed_seconds < timeout + FINALIZATION_RESERVE_SECONDS:
                raise StageCError(f"insufficient campaign time before {check_id}")
            check_dir = os.path.join(evidence_root, "checks", check_id)
            receipt_chain = _ACTIVE_GLOBAL_RECEIPT_CHAIN
            if receipt_chain is None:
                raise StageCError("global receipt chain disappeared before contained run")
            run_context = _v5_reserve_run(
                check_id,
                check_argv,
                check_dir,
                common,
                last_receipt,
            )
            process = _run_contained_wsl(
                check_id,
                check_argv,
                timeout,
                check_dir,
                common,
                predecessor=last_receipt,
                receipt_chain=receipt_chain,
                run_id=str(run_context["run_id"]),
                run_identity_material=dict(run_context["material"]),
            )
            returned_context = process.pop("_v5_run_context")
            if returned_context is not run_context:
                raise StageCError("contained run returned a different reservation")
            completed = _v5_complete_contained_check(
                check_id=check_id,
                ordinal=ordinal,
                process=process,
                run_context=run_context,
                check_dir=check_dir,
                evidence_root=evidence_root,
                common=common,
            )
            check_results[check_id] = completed["result"]
            check_records[check_id] = completed["result_record"]
            snapshots.append(completed["snapshot"])
            snapshot_labels.append(check_id)
            snapshot_records.append(completed["snapshot_record"])
            run_consumer_records[check_id] = completed["consumer_state"]
            if receipt_chain.head is None:
                raise StageCError("contained run completed without a global receipt head")
            last_receipt = dict(receipt_chain.head)

        current_phase = "final-snapshot"
        final_snapshot = _host_snapshot(
            "final", include_os=True, predecessor=last_receipt
        )
        final_snapshot_record = _atomic_json(
            os.path.join(evidence_root, "snapshots", "final.json"), final_snapshot
        )
        if _ACTIVE_GLOBAL_RECEIPT_CHAIN is None or _ACTIVE_GLOBAL_RECEIPT_CHAIN.head is None:
            raise StageCError("final snapshot did not advance the global chain")
        last_receipt = dict(_ACTIVE_GLOBAL_RECEIPT_CHAIN.head)
        snapshots.append(final_snapshot)
        snapshot_labels.append("final")
        snapshot_records.append(final_snapshot_record)
        if first_snapshot["os_identity"] != final_snapshot["os_identity"]:
            raise StageCError("OS/kernel/architecture changed during Stage C")
        c04_names = check_results["C04"]["semantic"]["names"]
        c05_names = check_results["C05"]["semantic"]["names"]
        if c04_names != c05_names:
            raise StageCError(f"C04/C05 ordinal name mismatch: {c04_names!r} != {c05_names!r}")
        activation_events = _activation_events(snapshots, snapshot_labels)
        activation_observed = any(
            bool(event["query_triggered_candidate"])
            for category in ("service", "process")
            for event in activation_events[category]
        )
        activation_allowed = preflight["authority_fields"][
            "query_triggered_service_activation_allowed"
        ]
        if activation_observed and not activation_allowed:
            raise StageCError("query-associated WSL service transition was not authorized")
        if activation_events["path"]:
            raise StageCError(
                f"registered host path identity changed during Stage C: {activation_events['path']!r}"
            )
        if activation_events["os"]:
            raise StageCError(
                f"host OS/kernel identity changed during Stage C: {activation_events['os']!r}"
            )
        unattributed_host_events = [
            event
            for category in ("service", "process")
            for event in activation_events[category]
            if not event["query_triggered_candidate"]
        ]
        post_c03_snapshot = snapshots[snapshot_labels.index("C03")]
        running_service = any(
            row.get("exists") and row.get("state") == 4
            for row in post_c03_snapshot["services"]
        )
        if not running_service:
            raise StageCError("C03 did not establish a functioning running WSL service")
        v4_inventory_final = _snapshot_v4_root()
        if v4_inventory_final != preflight["v4_inventory_pre"]:
            raise StageCError("immutable V4 evidence root changed during Stage C")
        report = {
            "schema": SCHEMA_REPORT,
            **common,
            "predecessor": _receipt_ref(last_receipt),
            "source_commit": "82a9db28d67507c82ef15c631f582a0c3bf6740e",
            "source_tree": "00b2b20691e73a05589b797b32352f1c760a2451",
            "checks": {
                check_id: {
                    "result_path": os.path.join(evidence_root, "checks", check_id, "result.json"),
                    "result_receipt": _receipt_ref(check_records[check_id]),
                    "run_consumer_state": (
                        None
                        if check_id == "C01"
                        else run_consumer_records[check_id]
                    ),
                    "success": bool(check_results[check_id]["success"]),
                }
                for check_id, _, _ in CHECKS
            },
            "snapshot_receipts": [
                _receipt_ref(record) for record in snapshot_records
            ],
            "c01_receipt_chain": list(c01_receipt_chain),
            "v4_inventory_pre": preflight["v4_inventory_pre"],
            "v4_inventory_final": v4_inventory_final,
            "wsl_version": EXPECTED_WSL_VERSION,
            "default_wsl_version": 2,
            "distribution_names": c05_names,
            "builder_distro_absent": BUILDER_DISTRO not in c05_names,
            "final_distro_absent": FINAL_DISTRO not in c05_names,
            "registered_paths_final": final_snapshot["paths"],
            "os_identity_pre": first_snapshot["os_identity"],
            "os_identity_final": final_snapshot["os_identity"],
            "activation_events": activation_events,
            "query_triggered_service_activation": activation_observed,
            "unattributed_host_events": unattributed_host_events,
            "host_state_unchanged": not any(activation_events.values()),
            "success": True,
            "finished_utc": _utc(),
            "wall_milliseconds": (time.monotonic_ns() - started_ns) // 1_000_000,
        }
        if run_context is None or run_context.get("check_id") != "C05":
            raise StageCError("C05 run context is unavailable at campaign success")
        run_consumer_records["C05"] = _v5_finalize_run_consumers(
            run_context,
            lane="c05_success",
        )
        report["checks"]["C05"]["run_consumer_state"] = run_consumer_records["C05"]
        return {
            "exit_code": 0,
            "stream": "stdout",
            "terminal_path": os.path.join(evidence_root, "stage_c_result.json"),
            "terminal_run_id": str(run_context["run_id"]),
            "terminal_consumer_id": (
                f"run:{run_context['run_id']}:top-level-success-published"
            ),
            "payload": report,
        }
    except (_ReceiptRegistrationLost, _ContainmentProofLost):
        raise
    except BaseException as exc:
        if run_context is not None and run_context.get("check_id") == "C05":
            chain = _ACTIVE_GLOBAL_RECEIPT_CHAIN
            if chain is not None:
                run = chain.require_contained_run(str(run_context["run_id"]))
                if run.get("expected_consumer_ids") is None:
                    consumer_state = _v5_finalize_run_consumers(
                        run_context,
                        lane="postprocess_failure",
                    )
                else:
                    consumer_state = chain.run_summary(str(run_context["run_id"]))
                setattr(exc, "run_id", str(run_context["run_id"]))
                setattr(exc, "run_consumer_manifest", consumer_state)
        exception_receipt = getattr(exc, "terminal_receipt", None)
        terminal_predecessor = exception_receipt or last_receipt
        failure = {
            "schema": SCHEMA_FAILURE,
            "phase": current_phase,
            "error_type": type(exc).__name__,
            "error": str(exc),
            "utc": _utc(),
            "wall_milliseconds": (time.monotonic_ns() - started_ns) // 1_000_000,
            "pid": os.getpid(),
            "root_created": root_created,
            "first_failure_preserved": True,
            "run_id": getattr(exc, "run_id", None),
            "run_consumer_manifest": getattr(exc, "run_consumer_manifest", None),
            "ordinary_prejob_failure": getattr(
                exc, "ordinary_prejob_failure", None
            ),
            "predecessor": (
                _receipt_ref(terminal_predecessor)
                if terminal_predecessor is not None
                else None
            ),
        }
        if common is not None:
            failure.update(common)
        failure["c01_receipt_chain"] = list(
            getattr(exc, "c01_receipt_chain", c01_receipt_chain)
        )
        if root_created:
            try:
                v4_inventory_final = _snapshot_v4_root()
                failure["v4_inventory_final"] = {
                    "captured": True,
                    "value": v4_inventory_final,
                    "matches_preflight": (
                        common is not None
                        and v4_inventory_final == common.get("v4_inventory_pre")
                    ),
                }
            except BaseException as inventory_exc:
                failure["v4_inventory_final"] = {
                    "captured": False,
                    "error": _error_record(inventory_exc),
                }
        terminal_path: str | None = None
        if root_created:
            observations: tuple[tuple[str, Any], ...] = (
                ("terminal_paths", _registered_absence_snapshot),
                ("terminal_services", _service_snapshot),
                ("terminal_processes", _process_snapshot),
                ("terminal_resources", _resource_snapshot),
            )
            for field, producer in observations:
                try:
                    failure[field] = {
                        "captured": True,
                        "value": producer(),
                    }
                except BaseException as observation_exc:
                    failure[field] = {
                        "captured": False,
                        "error_type": type(observation_exc).__name__,
                        "error": str(observation_exc),
                    }
            terminal_path = os.path.join(args.evidence_root, "stage_c_failure.json")
        return {
            "exit_code": 1,
            "stream": "stderr",
            "terminal_path": terminal_path,
            "terminal_run_id": getattr(exc, "run_id", None),
            "terminal_consumer_id": (
                None
                if getattr(exc, "run_id", None) is None
                else f"run:{getattr(exc, 'run_id')}:top-level-failure-published"
            ),
            "payload": failure,
        }


def _v5_fatal_frame_body(
    exc: _ReceiptRegistrationLost | _ContainmentProofLost,
    finalizer_outcome: Mapping[str, Any],
) -> bytes:
    promoted = getattr(exc, "promoted_receipt", None)
    prior = getattr(exc, "prior_receipt", None)
    containment = getattr(exc, "containment", None)
    frame: dict[str, Any] = {
        "schema": (
            SCHEMA_REGISTRATION_LOSS_FATAL
            if isinstance(exc, _ReceiptRegistrationLost)
            else SCHEMA_CONTAINMENT_PROOF_LOSS_FATAL
        ),
        "attempt_id": (
            getattr(exc, "attempt_id", None)
            if getattr(exc, "attempt_id", None) is not None
            else None
            if _ACTIVE_GLOBAL_RECEIPT_CHAIN is None
            else _ACTIVE_GLOBAL_RECEIPT_CHAIN.attempt_id
        ),
        "event": (
            "registration_loss"
            if isinstance(exc, _ReceiptRegistrationLost)
            else "containment_proof_loss"
        ),
        "created_utc": _utc(),
        "fatal_kind": type(exc).__name__,
        "exit_code": int(exc.exit_code),
        "phase": getattr(exc, "phase", "unknown"),
        "run_id": getattr(exc, "run_id", None),
        "attempted_consumer_id": getattr(exc, "attempted_consumer_id", None),
        "promoted_receipt": promoted,
        "prior_receipt": prior,
        "durable_head": getattr(exc, "durable_head", prior),
        "primary_error_type": getattr(exc, "cause_type", type(exc).__name__),
        "primary_message_sha256": getattr(
            exc,
            "cause_message_sha256",
            hashlib.sha256(str(exc).encode("utf-8")).hexdigest(),
        ),
        "containment_owner": (
            None if containment is None else containment.get("owner")
        ),
        "containment_terminal": (
            None if containment is None else containment.get("terminal")
        ),
        "containment_zero_pid": (
            None if containment is None else containment.get("zero_pid")
        ),
        "containment_errors": (
            [] if containment is None else containment.get("containment_errors", [])
        ),
        "job_identity": None if containment is None else containment.get("job_identity"),
        "pid": None if containment is None else containment.get("pid"),
        "process_creation_identity": (
            None if containment is None else containment.get("process_creation_identity")
        ),
        "stage_c_failure_published": False,
        "success_report_published": False,
        "host_successor_promotion_allowed": False,
        "retry_allowed": False,
        "cleanup_allowed": False,
        "campaign_wsl_hold_release_outcome": dict(finalizer_outcome),
        "global_receipt_chain": getattr(exc, "global_receipt_chain", None),
        "catalog_cleanup_errors": getattr(exc, "catalog_cleanup_errors", []),
        "source_artifact": getattr(exc, "source_artifact", None),
        "ordinary_prejob_failure": getattr(exc, "ordinary_prejob_failure", None),
        "run_consumer_manifest": getattr(exc, "run_consumer_manifest", None),
        "c01_pending_raw_events": getattr(exc, "c01_pending_raw_events", []),
        "truncated": False,
    }
    encoded = _canonical_json(frame)
    cap = 16_384
    if len(encoded) <= cap:
        return encoded
    frame["containment_errors"] = [
        {
            "omitted_count": len(frame["containment_errors"]),
            "sha256": hashlib.sha256(
                _canonical_json(frame["containment_errors"])
            ).hexdigest(),
        }
    ]
    frame["truncated"] = True
    frame["truncated_detail_sha256"] = hashlib.sha256(encoded).hexdigest()
    encoded = _canonical_json(frame)
    if len(encoded) > cap:
        raise StageCError("mandatory fatal stderr frame exceeds its fixed byte cap")
    return encoded


def _v5_fatal_frame(
    exc: _ReceiptRegistrationLost | _ContainmentProofLost,
    finalizer_outcome: Mapping[str, Any],
) -> bytes:
    """Return one bounded fatal frame without ever changing exit 86/87."""

    cap = 16_384
    try:
        full = _v5_fatal_frame_body(exc, finalizer_outcome)
        if len(full) <= cap:
            return full
        reduced = {
            "schema": (
                SCHEMA_REGISTRATION_LOSS_FATAL
                if isinstance(exc, _ReceiptRegistrationLost)
                else SCHEMA_CONTAINMENT_PROOF_LOSS_FATAL
            ),
            "fatal_kind": type(exc).__name__,
            "exit_code": int(exc.exit_code),
            "attempt_id": (
                getattr(exc, "attempt_id", None)
                if getattr(exc, "attempt_id", None) is not None
                else None
                if _ACTIVE_GLOBAL_RECEIPT_CHAIN is None
                else _ACTIVE_GLOBAL_RECEIPT_CHAIN.attempt_id
            ),
            "phase": getattr(exc, "phase", "unknown"),
            "run_id": getattr(exc, "run_id", None),
            "attempted_consumer_id": getattr(exc, "attempted_consumer_id", None),
            "promoted_receipt": getattr(exc, "promoted_receipt", None),
            "prior_receipt": getattr(exc, "prior_receipt", None),
            "durable_head": getattr(exc, "durable_head", None),
            "primary_error_type": getattr(exc, "cause_type", type(exc).__name__),
            "primary_message_sha256": getattr(
                exc,
                "cause_message_sha256",
                hashlib.sha256(str(exc).encode("utf-8")).hexdigest(),
            ),
            "containment_owner": (
                None
                if getattr(exc, "containment", None) is None
                else exc.containment.get("owner")
            ),
            "containment_terminal": (
                None
                if getattr(exc, "containment", None) is None
                else exc.containment.get("terminal")
            ),
            "containment_zero_pid": (
                None
                if getattr(exc, "containment", None) is None
                else exc.containment.get("zero_pid")
            ),
            "containment_errors": (
                []
                if getattr(exc, "containment", None) is None
                else [
                    {
                        "count": len(exc.containment.get("containment_errors", [])),
                        "sha256": hashlib.sha256(
                            json.dumps(
                                exc.containment.get("containment_errors", []),
                                sort_keys=True,
                                separators=(",", ":"),
                                ensure_ascii=True,
                                default=str,
                            ).encode("utf-8")
                        ).hexdigest(),
                    }
                ]
            ),
            "job_identity": (
                None
                if getattr(exc, "containment", None) is None
                else exc.containment.get("job_identity")
            ),
            "pid": (
                None
                if getattr(exc, "containment", None) is None
                else exc.containment.get("pid")
            ),
            "process_creation_identity": (
                None
                if getattr(exc, "containment", None) is None
                else exc.containment.get("process_creation_identity")
            ),
            "stage_c_failure_published": False,
            "success_report_published": False,
            "host_successor_promotion_allowed": False,
            "retry_allowed": False,
            "cleanup_allowed": False,
            "campaign_wsl_hold_release_outcome": dict(finalizer_outcome),
            "catalog_cleanup_errors": getattr(exc, "catalog_cleanup_errors", []),
            "source_artifact": getattr(exc, "source_artifact", None),
            "ordinary_prejob_failure": getattr(exc, "ordinary_prejob_failure", None),
            "run_consumer_manifest": getattr(exc, "run_consumer_manifest", None),
            "c01_pending_raw_events": getattr(exc, "c01_pending_raw_events", []),
            "truncated": True,
            "truncated_full_frame_sha256": hashlib.sha256(full).hexdigest(),
        }
        encoded = json.dumps(
            reduced,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
            default=lambda value: {
                "unserializable_type": type(value).__name__,
                "repr_sha256": hashlib.sha256(repr(value).encode("utf-8")).hexdigest(),
            },
        ).encode("utf-8") + b"\n"
        if len(encoded) <= cap:
            return encoded
    except BaseException:
        pass
    code = int(getattr(exc, "exit_code", 87))
    kind = (
        "receipt_registration_lost"
        if isinstance(exc, _ReceiptRegistrationLost)
        else "containment_proof_lost"
    )
    fallback_schema = (
        SCHEMA_REGISTRATION_LOSS_FATAL
        if isinstance(exc, _ReceiptRegistrationLost)
        else SCHEMA_CONTAINMENT_PROOF_LOSS_FATAL
    )
    def safe_text(value: Any) -> str | None:
        return value if isinstance(value, str) and len(value) <= 256 else None

    def safe_value(value: Any, depth: int = 0) -> Any:
        if value is None or isinstance(value, (bool, int, float)):
            return value
        if isinstance(value, str):
            return value[:1024]
        if depth >= 3:
            return {
                "evidence_limited_type": type(value).__name__,
                "repr_sha256": hashlib.sha256(repr(value).encode("utf-8")).hexdigest(),
            }
        if isinstance(value, Mapping):
            return {
                str(key)[:128]: safe_value(child, depth + 1)
                for key, child in list(value.items())[:32]
            }
        if isinstance(value, (list, tuple)):
            return [safe_value(child, depth + 1) for child in list(value)[:32]]
        return {
            "evidence_limited_type": type(value).__name__,
            "repr_sha256": hashlib.sha256(repr(value).encode("utf-8")).hexdigest(),
        }

    containment = getattr(exc, "containment", None)
    fallback = {
        "schema": fallback_schema,
        "fatal_kind": kind,
        "exit_code": code,
        "attempt_id": safe_text(getattr(exc, "attempt_id", None)),
        "phase": safe_text(getattr(exc, "phase", None)) or "fatal_frame_encoding",
        "run_id": safe_text(getattr(exc, "run_id", None)),
        "attempted_consumer_id": safe_text(
            getattr(exc, "attempted_consumer_id", None)
        ),
        "promoted_receipt": safe_value(getattr(exc, "promoted_receipt", None)),
        "prior_receipt": safe_value(getattr(exc, "prior_receipt", None)),
        "durable_head": safe_value(getattr(exc, "durable_head", None)),
        "primary_error_type": safe_text(getattr(exc, "cause_type", None))
        or "FatalFrameEncodingFailure",
        "primary_message_sha256": safe_text(
            getattr(exc, "cause_message_sha256", None)
        ),
        "containment_owner": (
            None if not isinstance(containment, Mapping) else safe_text(containment.get("owner"))
        ),
        "containment_terminal": (
            None if not isinstance(containment, Mapping) else containment.get("terminal") is True
        ),
        "containment_zero_pid": (
            None if not isinstance(containment, Mapping) else containment.get("zero_pid") is True
        ),
        "containment_errors": (
            []
            if not isinstance(containment, Mapping)
            else safe_value(containment.get("containment_errors", []))
        ),
        "job_identity": (
            None if not isinstance(containment, Mapping) else safe_value(containment.get("job_identity"))
        ),
        "pid": None if not isinstance(containment, Mapping) else safe_value(containment.get("pid")),
        "process_creation_identity": (
            None
            if not isinstance(containment, Mapping)
            else safe_value(containment.get("process_creation_identity"))
        ),
        "stage_c_failure_published": False,
        "success_report_published": False,
        "host_successor_promotion_allowed": False,
        "evidence_limited": True,
        "retry_allowed": False,
        "cleanup_allowed": False,
        "source_artifact": safe_value(getattr(exc, "source_artifact", None)),
        "ordinary_prejob_failure": safe_value(
            getattr(exc, "ordinary_prejob_failure", None)
        ),
        "run_consumer_manifest": safe_value(
            getattr(exc, "run_consumer_manifest", None)
        ),
        "c01_pending_raw_events": safe_value(
            getattr(exc, "c01_pending_raw_events", [])
        ),
    }
    return json.dumps(
        fallback,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("ascii") + b"\n"


def _campaign_wsl_hold_state() -> dict[str, Any]:
    return {
        "active": _CAMPAIGN_WSL_HANDLE is not None,
        "handle_value": (
            None
            if _CAMPAIGN_WSL_HANDLE is None
            else _handle_int(_CAMPAIGN_WSL_HANDLE)
        ),
        "frozen_identity": (
            None
            if _CAMPAIGN_WSL_FROZEN_IDENTITY is None
            else dict(_CAMPAIGN_WSL_FROZEN_IDENTITY)
        ),
    }


def _capture_campaign_wsl_hold_release(
    error: BaseException | None,
    *,
    attempted: bool,
    started_utc: str,
    finished_utc: str,
    pre_state: Mapping[str, Any],
    post_state: Mapping[str, Any],
) -> _CampaignWslHoldReleaseOutcome:
    success = error is None and post_state.get("active") is False
    error_record = None if error is None else _error_record(error)
    return _CampaignWslHoldReleaseOutcome(
        schema=(
            "anysolver.no_numba_residual.stage_c."
            "campaign_wsl_hold_release_outcome/1"
        ),
        attempted=attempted,
        success=success,
        started_utc=started_utc,
        finished_utc=finished_utc,
        pre_hold_state=dict(pre_state),
        post_hold_state=dict(post_state),
        failure_phase=(None if error is None else "campaign_wsl_hold_release"),
        failure_type=(None if error is None else type(error).__name__),
        failure_code=(
            None
            if error is None
            else getattr(error, "winerror", getattr(error, "errno", None))
        ),
        failure_message_sha256=(
            None
            if error is None
            else hashlib.sha256(str(error).encode("utf-8")).hexdigest()
        ),
        error=error_record,
    )


def main(argv: Sequence[str] | None = None) -> int:
    global _ACTIVE_GLOBAL_RECEIPT_CHAIN

    pending: _PendingStageCOutcome | None = None
    selected_exit = 1
    fatal: _ReceiptRegistrationLost | _ContainmentProofLost | None = None
    finalizer_error: BaseException | None = None
    finalizer_attempted = False
    finalizer_started_utc = _utc()
    finalizer_finished_utc = finalizer_started_utc
    finalizer_pre_state: dict[str, Any] = _campaign_wsl_hold_state()
    finalizer_post_state: dict[str, Any] = dict(finalizer_pre_state)
    try:
        with _HardDeadline(DEADLINE_SECONDS, 0xE000C011, "campaign"):
            try:
                pending = _PendingStageCOutcome(_main_impl(argv))
                selected_exit = int(pending["exit_code"])
            except (_ReceiptRegistrationLost, _ContainmentProofLost) as exc:
                fatal = exc
                selected_exit = int(exc.exit_code)
    except BaseException as exc:
        if fatal is not None:
            selected_exit = int(fatal.exit_code)
            setattr(fatal, "outer_boundary_error", _error_record(exc))
        else:
            selected_exit = 1
            pending = _PendingStageCOutcome({
                "exit_code": 1,
                "stream": "stderr",
                "terminal_path": None,
                "payload": {
                    "schema": SCHEMA_FAILURE,
                    "phase": "campaign_deadline_or_outer_boundary",
                    "error": _error_record(exc),
                    "utc": _utc(),
                    "root_created": _ACTIVE_GLOBAL_RECEIPT_CHAIN is not None,
                    "first_failure_preserved": True,
                },
            })
    finally:
        finalizer_started_utc = _utc()
        finalizer_pre_state = _campaign_wsl_hold_state()
        if _CAMPAIGN_WSL_HANDLE is not None:
            finalizer_attempted = True
            try:
                _release_campaign_wsl_hold()
            except BaseException as exc:
                # A release error is terminal evidence but never replaces the
                # already selected 0/1/86/87 outcome and never triggers a second
                # receipt or fatal-frame publication.
                finalizer_error = exc
        finalizer_finished_utc = _utc()
        finalizer_post_state = _campaign_wsl_hold_state()

    finalizer_outcome = _capture_campaign_wsl_hold_release(
        finalizer_error,
        attempted=finalizer_attempted,
        started_utc=finalizer_started_utc,
        finished_utc=finalizer_finished_utc,
        pre_state=finalizer_pre_state,
        post_state=finalizer_post_state,
    )
    chain = _ACTIVE_GLOBAL_RECEIPT_CHAIN
    if fatal is not None:
        if getattr(fatal, "containment", None) is None:
            fatal_run_id = getattr(fatal, "run_id", None)
            if fatal_run_id is not None and chain is not None:
                try:
                    _v5_attach_retained_proof(fatal, str(fatal_run_id))
                except BaseException as proof_exc:
                    prior_fatal = fatal
                    fatal = _ContainmentProofLost(
                        phase="outer_fatal_missing_contained_proof",
                        run_id=str(fatal_run_id),
                        durable_head=(None if chain.head is None else dict(chain.head)),
                        promoted_receipt=getattr(fatal, "promoted_receipt", None),
                        cause=proof_exc,
                        containment={
                            "owner": "outer_fatal",
                            "reason": "contained_proof_unavailable",
                            "child_created": {
                                "status": "unknown_after_creation_attempt"
                            },
                            "terminal": False,
                            "zero_pid": False,
                            "handles_closed": False,
                            "job_identity": {
                                "status": "unknown_after_creation_attempt"
                            },
                            "pid": {"status": "unknown_after_creation_attempt"},
                            "process_creation_identity": {
                                "status": "unknown_after_creation_attempt"
                            },
                            "containment_errors": [_error_record(proof_exc)],
                        },
                    )
                    fatal.attempt_id = getattr(prior_fatal, "attempt_id", None)
                    fatal.attempted_consumer_id = getattr(
                        prior_fatal, "attempted_consumer_id", None
                    )
                    fatal.source_artifact = getattr(
                        prior_fatal, "source_artifact", None
                    )
                    fatal.run_consumer_manifest = getattr(
                        prior_fatal, "run_consumer_manifest", None
                    )
                    selected_exit = fatal.exit_code
            else:
                fatal.containment = {
                    "owner": "campaign_no_child",
                    "reason": "host_only_before_contained_run",
                    "child_created": False,
                    "terminal": True,
                    "zero_pid": True,
                    "handles_closed": True,
                    "job_identity": None,
                    "pid": None,
                    "process_creation_identity": None,
                    "containment_errors": [],
                }
        if chain is not None:
            fatal.global_receipt_chain = chain.summary()
        try:
            os.write(2, _v5_fatal_frame(fatal, finalizer_outcome))
        except BaseException:
            # The external caller owns raw stderr/process capture.  A local
            # stderr failure must never collapse the selected fatal exit.
            pass
        _ACTIVE_GLOBAL_RECEIPT_CHAIN = None
        return selected_exit

    if pending is None:
        pending = _PendingStageCOutcome({
            "exit_code": 1,
            "stream": "stderr",
            "terminal_path": None,
            "payload": {
                "schema": SCHEMA_FAILURE,
                "phase": "main",
                "error_type": "MissingPendingOutcome",
                "error": "main returned without a pending outcome",
                "utc": _utc(),
            },
        })
        selected_exit = 1

    payload = dict(pending["payload"])
    payload["campaign_wsl_hold_release_outcome"] = finalizer_outcome
    payload["selected_exit_code"] = selected_exit
    payload["selected_outcome_preserved"] = True
    payload["terminal_outside_global_chain"] = True
    payload["predecessor"] = None if chain is None or chain.head is None else dict(chain.head)
    payload["global_receipt_chain"] = (
        [] if chain is None else list(chain.summary()["nodes"])
    )
    terminal_path = pending.get("terminal_path")
    terminal_receipt: dict[str, Any] | None = None
    if terminal_path is not None:
        try:
            terminal_receipt = _atomic_terminal_json(str(terminal_path), payload)
            terminal_run_id = pending.get("terminal_run_id")
            terminal_consumer_id = pending.get("terminal_consumer_id")
            if (
                chain is not None
                and terminal_run_id is not None
                and terminal_consumer_id is not None
            ):
                chain.mark_top_level_publication(
                    str(terminal_run_id),
                    str(terminal_consumer_id),
                    terminal_receipt,
                )
        except (_ReceiptRegistrationLost, _ContainmentProofLost) as terminal_fatal:
            terminal_run_id = pending.get("terminal_run_id")
            if (
                getattr(terminal_fatal, "containment", None) is None
                and terminal_run_id is not None
                and chain is not None
            ):
                try:
                    _v5_attach_retained_proof(terminal_fatal, str(terminal_run_id))
                except BaseException:
                    pass
            if chain is not None:
                terminal_fatal.global_receipt_chain = chain.summary()
            try:
                os.write(2, _v5_fatal_frame(terminal_fatal, finalizer_outcome))
            except BaseException:
                pass
            _ACTIVE_GLOBAL_RECEIPT_CHAIN = None
            return int(terminal_fatal.exit_code)
        except BaseException as exc:
            selected_exit = 1
            payload = {
                "schema": SCHEMA_FAILURE,
                "selected_exit_code": selected_exit,
                "terminal_path": terminal_path,
                "error": _error_record(exc),
                "campaign_wsl_hold_release_outcome": finalizer_outcome,
                "global_receipt_chain": None if chain is None else chain.summary(),
                "second_publication_attempted": False,
                "retry_allowed": False,
                "cleanup_allowed": False,
            }
            pending["stream"] = "stderr"

    message = {
        "success": selected_exit == 0,
        "selected_exit_code": selected_exit,
        "terminal": None if terminal_receipt is None else _receipt_ref(terminal_receipt),
        "payload": payload,
    }
    try:
        encoded = _canonical_json(message) + b"\n"
    except BaseException as exc:
        selected_exit = 1
        encoded = (
            f"{{\"schema\":\"{SCHEMA_FAILURE}\"," 
            "\"selected_exit_code\":1,\"evidence_limited\":true,"
            f"\"message_sha256\":\"{hashlib.sha256(str(exc).encode('utf-8')).hexdigest()}\"}}\n"
        ).encode("ascii")
        pending["stream"] = "stderr"
    try:
        os.write(1 if pending["stream"] == "stdout" else 2, encoded)
    except BaseException:
        pass
    _ACTIVE_GLOBAL_RECEIPT_CHAIN = None
    return selected_exit


if __name__ == "__main__":
    raise SystemExit(main())
