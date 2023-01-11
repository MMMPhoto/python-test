helloFile = open('./exercises/fileReadWrite/hello.txt')
content = helloFile.read()
print(content)

helloNewFile = open('./exercises/fileReadWrite/newFileTest.txt', 'a')
helloNewFile.write('Hello!\n')
helloNewFile.write('Hello!\n')
helloNewFile.write('Hello World!\n')