from views import Index, About, Products, Contacts

# Набор привязок: путь-контроллер
routes = {
    '/': Index(),
    '/about/': About(),
    '/products/': Products(),
    '/contacts/': Contacts()
}
