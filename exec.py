import os
import subprocess

def execute():
    # 获取当前脚本的目录
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # 定位 fourier.py 的路径
    fourier_script = os.path.join(current_directory, "fourier.py")
    # 执行 fourier.py
    try:
        subprocess.run(["python", fourier_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing fourier.py: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # 定位 laplace.py 的路径
    laplace_script = os.path.join(current_directory, "laplace.py")
    # 执行 laplace.py
    try:
        subprocess.run(["python", laplace_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing laplace.py: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # 定位 z.py 的路径
    z_script = os.path.join(current_directory, "z.py")
    # 执行 z.py
    try:
        subprocess.run(["python", z_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing z.py: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # 定位 db6.py 的路径
    db6_script = os.path.join(current_directory, "db6.py")
    # 执行 db6.py
    try:
        subprocess.run(["python", db6_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing db6.py: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # 定位 wavelet.py 的路径
    wavelet_script = os.path.join(current_directory, "wavelet.py")
    # 执行 wavelet.py
    try:
        subprocess.run(["python", wavelet_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing wavelet.py: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # 定位 ftfr.py 的路径
    ftfr_script = os.path.join(current_directory, "ftfr.py")
    # 执行 ftfr.py
    try:
        subprocess.run(["python", ftfr_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing ftfr.py: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    execute()
