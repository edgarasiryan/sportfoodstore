from .models import Category

def categories(request):
    """
    Returns a context dictionary containing top-level categories.

    This function retrieves all categories with no parent from the database
    and returns them in a dictionary to be used as context data in templates.

    Args:
        request: The HTTP request object.

    Returns:
        A dictionary with a single key 'categories' mapped to a queryset
        of Category objects that have no parent.
    """

    categories = Category.objects.filter(parent=None)
    return {'categories': categories}