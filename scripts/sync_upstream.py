"""
Script tu dong kiem tra va dong bo cap nhat tu repo goc (upstream) DataTalksClub:
1. Keo cac cap nhat moi nhat tu repo goc ve nhanh phu 'english' (ban tieng Anh goc).
2. Dong bo va merge cac cap nhat tu 'english' vao nhanh chinh 'main' (ban tieng Viet).
3. Day (push) ca 2 nhanh len GitHub ca nhan.
4. Thong bao danh sach file moi/thay doi de tien hanh dich noi dung moi sang tieng Viet.
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
    print("==================================================================")
    print("   KIEM TRA VA DONG BO CAP NHAT TU REPO GOC (UPSTREAM)")
    print("   - Nhanh phu 'english': Luu tru ban goc tieng Anh tu DataTalksClub")
    print("   - Nhanh chinh 'main': Ban dich tieng Viet phuc vu hoc tap")
    print("==================================================================\n")

    # 1. Kiem tra va them remote upstream neu chua co
    remotes = subprocess.run("git remote", shell=True, text=True, capture_output=True).stdout.split()
    if "upstream" not in remotes:
        print("Chua co remote upstream. Dang them remote upstream...")
        run_cmd("git remote add upstream https://github.com/DataTalksClub/data-engineering-zoomcamp.git")
    else:
        print("[OK] Da ket noi remote upstream.")

    # 2. Fetch du lieu moi tu upstream
    print("\nDang kiem tra du lieu moi tu DataTalksClub...")
    run_cmd("git fetch upstream")

    # 3. Kiem tra so commit moi so voi nhanh english
    diff_res = subprocess.run("git log english..upstream/main --oneline", shell=True, text=True, capture_output=True)
    commits = diff_res.stdout.strip().splitlines() if diff_res.stdout.strip() else []

    if not commits:
        print("\n[OK] Nhanh 'english' va 'main' da hoan toan khop voi ban moi nhat tu repo goc!")
        print("Khong co cap nhat moi nao tu DataTalksClub can xu ly.")
        return

    print(f"\n[!] Phat hien {len(commits)} commit moi tu repo goc:")
    for c in commits:
        print(f"   * {c}")

    # 4. Kiem tra cac file thay doi
    changed_files = subprocess.run(
        "git diff --name-only english upstream/main", shell=True, text=True, capture_output=True
    ).stdout.strip().splitlines()

    print("\nDanh sach cac file co thay doi/moi tu upstream:")
    for f in changed_files:
        print(f"   - {f}")

    # 5. Hoi nguoi dung co muon dong bo khong
    confirm = input("\nBan co muon tu dong pull ve 'english' va update sang 'main' (tieng Viet) khong? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Da huy thao tac dong bo.")
        return

    # 6. Cap nhat nhanh english (ban tieng Anh goc)
    print("\nDang cap nhat nhanh phu 'english'...")
    run_cmd("git checkout english")
    run_cmd("git pull upstream main")
    run_cmd("git push origin english")

    # 7. Merge cac thay doi tu english vao nhanh main (tieng Viet)
    print("\nDang merge cap nhat sang nhanh chinh 'main' (tieng Viet)...")
    run_cmd("git checkout main")
    run_cmd("git merge english -m 'merge: Dong bo cap nhat moi tu upstream vao ban tieng Viet'")
    run_cmd("git push origin main")

    print("\n[OK] Hoan tat dong bo!")
    print("1. Nhanh 'english' da luu tru ban goc tieng Anh moi nhat.")
    print("2. Nhanh 'main' da nhan cac tap tin va cap nhat moi.")
    print("\nBan hay nhan vao hop chat AI de nho AI dich ngay cac file moi sang tieng Viet!")

if __name__ == "__main__":
    main()
