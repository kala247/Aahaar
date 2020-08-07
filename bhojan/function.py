def handle_uploaded_file(f):
    destination = open('images', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()