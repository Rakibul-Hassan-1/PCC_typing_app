def save_typing_data(request, speed, accuracy):
    if request.user.is_authenticated:
        TypingData.objects.create(
            user=request.user,
            speed=speed,
            accuracy=accuracy
        )
        print(f"Data saved: {speed} WPM, {accuracy}%")