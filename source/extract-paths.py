import os

uid = 1

def handle_svg_dir(dir, country=''):
  lines = []
  global uid
  for filename in os.listdir(dir):
    path = dir + '/' + filename
    if os.path.isdir(path):
      lines.append('\n'.join(handle_svg_dir(path, path.split('/')[-1])))
    else:
      with open(path, "r") as f:
        pathLines = f.readlines()
        # remove unused lines
        pathLines = pathLines[11:-2]
        # remove line breaks
        pathLines = [l[:-1] for l in pathLines]
        path_border = ' '.join(pathLines)

        path_fill = path_border.split('m')[0][:-1] + '" class="region-fill" />'
        path_border = path_border[:-2] + ' class="region-border" />'

        lines.append('<g id="' + filename[:-4] + '" data-uid="' + str(uid) + '" class="region ' + country + '">')
        lines.append('<title>' + filename[:-4] + '</title>')
        lines.append(path_fill)
        lines.append(path_border)
        lines.append('</g>\n')
        uid = uid + 1
  return lines

def write_paths(content):
  with open("template.html", "r") as input:
    lines = input.readlines()
    with open("index.html", "w") as out:
      for l in lines:
        out.write(l.replace("%PATHS%", content))

paths = handle_svg_dir('svg/')
content = '\n'.join(paths)
write_paths(content)