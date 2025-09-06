#pragma once

// Stop game close on debugger attach
void PatchAntiDebug()
{
    void* dbgBreak = GetProcAddress(GetModuleHandleA("ntdll.dll"), "DbgUiRemoteBreakin");

    if (dbgBreak)
    {
        DWORD old;
        VirtualProtect(dbgBreak, 1, PAGE_EXECUTE_READWRITE, &old);
        *(BYTE*)dbgBreak = 0xC3; // ret
        VirtualProtect(dbgBreak, 1, old, &old);
    }

    dbgBreak ? printf("Made By ntjq - Russi.\n") : printf("[-] Failed.\n");
}
