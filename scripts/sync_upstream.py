"""
Script tu dong kiem tra va dong bo cap nhat tu repo goc (upstream)
DataTalksClub/data-engineering-zoomcamp ve nhanh main va vietnamese.
"""

import subprocess
import sys

# Dam bao tuong thich ma hoa UTF-8 tren Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def run_cmd(cmd, check=True):
    print(f"--> Dang chay: {cmd}")
    res = subprocess.run(cmd, shell=True, text=True, capture_output=True, encoding="utf-8", errors="replace")
    if res.stdout:
        print(res.stdout.strip())
    if res.stderr and res.returncode != 0:
        print(f"Loi: {res.stderr.strip()}", file=sys.stderr)
    if check and res.returncode != 0:
        sys.exit(res.returncode)
    return res

def main():
    print("==========================================================")
    print("   KIEM TRA VA DONG BO CAP NHAT TU REPO GOC (UPSTREAM)")
    print("==========================================================\n")

    # 1. Kiem tra va them remote upstream neu chua co
    remotes = subprocess.run("git remote", shell=True, text=True, capture_output=True).stdout.split()
    if "upstream" not in remotes:
        print("Chua co remote upstream. Dang them remote upstream...")
        run_cmd("git remote add upstream https://github.com/DataTalksClub/data-engineering-zoomcamp.git")
    else:
        print("[OK] Da ket noi remote upstream.")

    # 2. Fetch du lieu moi tu upstream
    print("\nDang tai du lieu moi nhat tu DataTalksClub...")
    run_cmd("git fetch upstream")

    # 3. Kiem tra so commit moi
    diff_res = subprocess.run("git log HEAD..upstream/main --oneline", shell=True, text=True, capture_output=True)
    commits = diff_res.stdout.strip().splitlines() if diff_res.stdout.strip() else []

    if not commits:
        print("\n[OK] Tuyet voi! Tai lieu cua ban da hoan toan khop voi ban moi nhat tu repo goc.")
        print("Khong co commit moi nao tu upstream can cap nhat.")
        return

    print(f"\n[!] Phat hien {len(commits)} commit moi tu repo goc:")
    for c in commits:
        print(f"   * {c}")

    # 4. Kiem tra cac file thay doi
    changed_files = subprocess.run(
        "git diff --name-only HEAD upstream/main", shell=True, text=True, capture_output=True
    ).stdout.strip().splitlines()

    print("\nDanh sach cac file co thay doi tu upstream:")
    for f in changed_files:
        print(f"   - {f}")

    # 5. Hoi nguoi dung co muon merge khong
    confirm = input("\nBan co muon tu dong merge cac thay doi nay vao main va vietnamese khong? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Da huy thao tac merge.")
        return

    # 6. Cap nhat main
    print("\nDang cap nhat nhanh main...")
    run_cmd("git checkout main")
    run_cmd("git pull upstream main")
    run_cmd("git push origin main")

    # 7. Merge vao vietnamese
    print("\nDang merge vao nhanh vietnamese...")
    run_cmd("git checkout vietnamese")
    run_cmd("git merge main -m 'merge: Dong bo cap nhat moi tu upstream/main'")
    run_cmd("git push origin vietnamese")

    print("\n[OK] Hoan tat dong bo!")
    print("Cac file moi da duoc cap nhat vao nhanh 'vietnamese'.")
    print("Ban chi can nhan vao hop chat AI de nho AI dich tiep cac file moi cap nhat!")

if __name__ == "__main__":
    main()
