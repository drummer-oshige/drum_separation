import argparse
import separation
import sys


def main(input_path, output_path, mode):
    if mode not in ['drum', 'melody']:
        print('modeはdrum or melodyを指定してください')
        sys.exit(1)
    try:
        y_harmonic, y_percussive, sr = separation.drum_separation(input_path)
        if mode == 'drum':
            separation.write(output_path, y_percussive, sr)
        else:
            separation.write(output_path, y_harmonic, sr)
        sys.exit(0)
    except Exception as e:
        print(str(e))
        sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='main.py',
        usage='python3 main.py --input [読み込みファイルのパス] --output [出力ファイルのパス]',
        add_help=True)
    parser.add_argument('-i', '--input',
                        help='読み込みファイルのパス',
                        type=str,
                        required=True)
    parser.add_argument('-o', '--output',
                        help='出力ファイルのパス',
                        type=str,
                        required=True)
    parser.add_argument('-m', '--mode',
                        help='[drum]=ドラムのみ抽出して出力, [melody]=ドラムを除去してメロディのみ出力',
                        type=str,
                        default='drum',
                        required=False)
    args = parser.parse_args()
    main(args.input, args.output, args.mode)
