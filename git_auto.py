import os
import shutil
import stat

def force_remove(path):
    def on_rm_error(func, path, exc_info):
        # 읽기 전용 파일이면 권한 수정 후 삭제 재시도
        os.chmod(path, stat.S_IWRITE)
        func(path)

    shutil.rmtree(path, onerror=on_rm_error)

def remove_git_dirs():
    base_path = os.getcwd()
    first = True

    for root, dirs, files in os.walk(base_path, topdown=True):
        if first:
            first = False
            continue

        if '.git' in dirs:
            git_path = os.path.join(root, '.git')
            print(f"삭제 중: {git_path}")
            force_remove(git_path)

if __name__ == "__main__":
    remove_git_dirs()
