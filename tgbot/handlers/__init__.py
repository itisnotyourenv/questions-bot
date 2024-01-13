"""Import all routers and add them to routers_list."""
from .admin import admin_router
from .echo import echo_router
from .user import user_router
from .question import question_router
from .answers import answer_router
from .image import image_router
from .replies import reply_router

routers_list = [
    admin_router,
    answer_router,
    user_router,
    image_router,
    question_router,
    reply_router,
    echo_router,  # echo_router must be last
]

__all__ = [
    "routers_list",
]
