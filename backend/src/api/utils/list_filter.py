from django_filters import Filter


class ListFilter(Filter):
    def filter(self, qs, value):
        if not value:
            return qs

        # For django-filter versions < 0.13, use lookup_type
        # instead of lookup_expr

        self.lookup_expr = 'in'
        values = value.split(',')
        return super(ListFilter, self).filter(qs, values)
