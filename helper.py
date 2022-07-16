import os
from PIL import Image


def get_file_path(root_path, file_list, dir_list):
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        dir_file_path = os.path.join(root_path, dir_file)
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            get_file_path(dir_file_path, file_list, dir_list)
        else:
            file_list.append(dir_file_path)
    return file_list


def handle_file(output_root_path, file_root_path):
    for i in range(len(file_root_path)):
        file_suffix = os.path.splitext(file_root_path[i])[1]
        if file_suffix == '.jpg' or file_suffix == '.png' or file_suffix == '.jpge':
            try:
                old_file_path = file_root_path[i]
                new_file_path = output_root_path + '/' + str(i) + file_suffix
                file_path = convert_to_webp(old_file_path, new_file_path)
                compress_image(file_path)
                print('old path: ' + old_file_path, 'new path: ' + file_path)
            except Exception as e:
                print(e)


def get_size(file):
    size = os.path.getsize(file)
    return size / 1024


def compress_image(infile, outfile=None, step=10, quality=80):
    if outfile is None:
        outfile = infile
    o_size = get_size(infile)
    if o_size <= config['compress_image_size']:
        image = Image.open(infile)
        image.save(outfile)

    while o_size > config['compress_image_size']:
        image = Image.open(infile)
        image = image.resize((image.size[0] // 2, image.size[1] // 2))
        image.save(outfile, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = get_size(outfile)


def convert_to_webp(infile, outfile=None):
    if outfile is None:
        outfile = infile
    if config['is_webp'] is True:
        image = Image.open(infile)
        image.save(os.path.splitext(outfile)[0]+'.webp', 'webp')
        print('image ' + infile + ' is turn to webp')
        return os.path.splitext(outfile)[0] + '.webp'
    return outfile


if __name__ == '__main__':
    root_path = input('Input you image path: ')
    config = {
        'root_path': root_path,
        'output_root_path': 'images',
        'compress_image_size': 800,
        'is_webp': True,
    }

    file_list = get_file_path(config['root_path'], [], [])
    handle_file(config['output_root_path'], file_list)
