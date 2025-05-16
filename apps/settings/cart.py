from decimal import Decimal
from apps.courses.models import Course


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart 
    
    def add(self, course, quantity=1, update_quantity=False):
        course_id = str(course.id)
        if course_id not in self.cart:
            self.cart[course_id] = {'quantity': 0, 'price': str(course.price)}
        if update_quantity:
            self.cart[course_id]['quantity'] = quantity
        else:
            self.cart[course_id]['quantity'] += quantity
        self.save()
    
    def save(self):
        if hasattr(self.session, 'modified'):
            self.session.modified = True
    
    def remove(self, course):
        course_id = str(course.id)
        if course_id in self.cart:
            del self.cart[course_id]
            self.save()

    def __iter__(self):
        course_ids = self.cart.keys()
        courses = Course.objects.filter(id__in=course_ids)
        courses_map = {str(course.id): course for course in courses}

        for course_id, item in self.cart.items():
            item_copy = item.copy()
            item_copy['course'] = courses_map.get(course_id)
            item_copy['total_price'] = Decimal(item['price']) * item['quantity']
            yield item_copy

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values()) 
    
    def clear(self):
        self.session.pop('cart', None)
        self.save()