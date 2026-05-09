class Phone:
    __is_5g_enable = True
    def __check_5g(self):
        if self.__is_5g_enable == True:
            print("5g activé")
        if self.__is_5g_enable == False:
            print("5g off, utilisation d'un réseau 4g")
        return self

    def call_by_5g(self):
        self.__check_5g()
        print("appel en cours")

phone1 = Phone()
phone1.call_by_5g()