# შექმენით ფუნქცია, რომელიც იღებს წინადადებას, და მასში space-ების მაგივრად სიტყვებს 
# შორის ჩასვამს ტირეს("-"). საბოლოოდ კი აბრუნებს მას

def space_in_sentence(text):
    cleaned_sentence = "-".join(text.split())
    return cleaned_sentence