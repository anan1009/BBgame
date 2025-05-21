html = '<div class="job">Senior Python Developer</div>'

start = html.find('>') + 1

end = html.find('</', start)

content = html[start:end]

print(content)