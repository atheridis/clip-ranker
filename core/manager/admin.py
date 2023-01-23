"""
Copyright (C) 2023  Georgios Atheridis <georgios@atheridis.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from django.contrib import admin

# Register your models here.
from .models import Clip, ResetData, AllowedChannel


class AllowedChannelInline(admin.TabularInline):
    model = AllowedChannel


class ResetDataAdmin(admin.ModelAdmin):
    inlines = [
        AllowedChannelInline,
    ]


admin.site.register(Clip)
admin.site.register(ResetData, ResetDataAdmin)
