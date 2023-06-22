from aiogram.dispatcher.filters.state import StatesGroup, State


class UserRegister(StatesGroup):
    Customer = State()
    City = State()
    Category = State()
    Subcategory = State()
    Finish = State()


class PurchaseRequest(StatesGroup):
    Photo = State()
    Info = State()
    Category = State()
    Subcategory = State()
    Finish = State()


class ServiceRequest(StatesGroup):
    Info = State()
    Category = State()
    Subcategory = State()
    Finish = State()


class SellerResponse(StatesGroup):
    Price = State()
    Finish = State()


class ServiceResponse(StatesGroup):
    Price = State()
    Finish = State()


class SellerChangeCategory(StatesGroup):
    Category = State()
    Subcategory = State()


class AdminGetUser(StatesGroup):
    Username = State()


class AdminSetUser(StatesGroup):
    Dict = State()


class AdminMailing(StatesGroup):
    Dict = State()
    Ad = State()