from App import app

if __name__ == '__main__':
    app.run(debug = True, port = 5050)

    '''
    User = {}
    User['gary'] = {
        "password":'1234',
        "email":"1234@gmail"
    }
    write_to_json_file(USERDATA, User)
    '''
