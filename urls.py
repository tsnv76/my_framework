from views import Index, About, Otchets, Contacts

# Набор привязок: путь-контроллер
routes = {
    '/': Index(),
    '/about/': About(),
    '/otchets/': Otchets(),
    '/contacts/': Contacts()
}
