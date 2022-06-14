if __name__ == '__main__':
    a = "Hello World!"
    try:
        a + 10
    except Exception:
        msg = "You can't add int to string"
    print(msg)
