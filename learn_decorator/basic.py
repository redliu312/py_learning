def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


def get_name(name):
    return name

@p_decorate
def fancy_get_name(name):
    return name


def main():
    print (get_name("john"))
    print (decorated_get_name("simon"))


def main():
    pass
    



if __name__=="__main__":
    main()
