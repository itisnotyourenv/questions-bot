from tasks.celery import celery_app

from image_generator.example import add_text_to_image


@celery_app.task()
def generate_image(user_id: int, text: str):
    print()
    print()
    print("GENERATING IMAGE...")
    path = add_text_to_image(text=text)
    print(f"{path=}")
    print()
    print()
