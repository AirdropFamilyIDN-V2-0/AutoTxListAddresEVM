import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("eJx9Vt1vG8cRv707Hj9F0fq2LFtrO45KR5VbFAUKIU2r6CMW4qiGSVfuFgax4o7JI++D3ltaEkE9KX0Mmj4nBqTHIn9E/4976EP75D+gDw0CpLN3J1syihxxe7czv5mdnf3NHP9tvHcV8P493tEz0zCEIYhn+IQR32Qm0XPTs5iVPG1mJ88cyyVPhzn4tLy8X2CFBGt7Rb/ESn6Zlf0Kq2T2E2wCKiInnK8IMaAKpd6kyM8bpxezmihcmk2K4hVd6YqufEV34YUAOTPhWoKoaNk5OSXMgKlMNqFlKJkG42zm3JDjzL6a2gf5zPtkOhc1ce1Lg81m1lNayuYybzUxnXmbh8LZAsydE3YdJnqLZzfEzDmJvst8zWa+zIYBS2JGzJ2af62wm3Dz7Na5wZb3UWMbtnFq4fqFXxrRPw4RrX9/whtotvZ8ttZtscDuiOti8UsD7goDPoDlUwJ3Tq0tHds9uLdlPP+cfQgf4vN3bAVWzn6Gq6zALO64Dtd7K+cE5pJ3/Xb71P6ayFtZFm7A/DeGWHptZdm8C/N4bje17+cL7H62n1twH1HLGiWouP0VsgPss4/EnXO0+Zq8LCTjnZf/yrzeTb29/KfOQP2DN5prdTO29+HgV3HlYbP5+LEMX7kC5F6dxPmNdjscBqpuxfZOKCHONdSxB7HtBq5q1gkr8qFCeQRqdO/PHz3/7U9fiEhgVF8bT5t/oM1ndPuPX9Avnj5q7m4+3Njd05orMARtbG092W40thsU9Y92G81EcRWG/ly5JcMB3eG+6x3T3a2992BdpQbR+oMHas2HB4gWiE7BGqthszg8goOwH4T0yeNN+lR6dJ1eEW92uRvsCi2eRrFOG9075v7BMOisra2NtJ/PeId776R0Mzzg1OcBdBHRti9V+QTeRbw3daUvEcNQxtgYmwrrZmwJco5vPatn6/EsNzbOiTC/dU7SuaPnJ7nkPT+28d15Zzd2UssZY944yY9z43zfkJ+pgir2SsJCXHmc1zjkjp3Mctks9zqXVYjTSKNxfjKe/Lf5k0IirZxNjAtjxJwUE311XOxNYlQlVUP7a+OSrv6TcqKb0rOTShLPtO4zYxP5m3WYLMrSuPyN8drMoikjWyt7LAeqC7LuxPl2ehCx/UKGfmyqMM694t4Q4kKHR4+l20ayBmHQhtEiHkmDeyKkoeS0PewPB+v0YKiGXTqap9vNh6s04EHHDTrUx/OiPOB0ZGvFTj0vdSOW+oyYhY5lSU/LeqjoQR/gaBkX2Ou40vW1EfUhOEZ/dJ97HijNlEVaQkhT8iDi/ciln4Ls8sj1NGESzbOf726t02Z9Jlkutg+RVsxRYesQXGbhnlkRF28N9LbYbAdUSyXO2soNg1ZSoqysxQfc47hnVoFIuT5X0EK7OIeGgZI57Tu3/3C3uc0KOm2J+zxPa5zVIrcTXHbMZiIIREvywyvSKgqa7+axFSmZBNuFI7Z0yF3VehHKKxFKaIM7ULH1ZHurPhE72i/IuJg++3DMighxBy4EKna4n8Tj6C2rI1ZNUW/3plOxkUJKKlTcwwREihUFDLzwWFsU0p0cBSyvjlqY6i6z1ZEr2PT/CervhpzTibF4FMZOc6eFZ7io6/E3OJiWSUxSIo6+v6+UKmSBFMxVYpNU81b331q5alatCpkjM6iVC5oYq5caB1LyFZ4H7vWCGLrxNbg/AGSLZsmvL6EPoa+GtAeCIx0Vx6iBqrf80VQVoNy+Npv03EhxIbALR2vqSI1W0M+O6wF9T5HQX7gK/LDP+7AWEzmqX1qzN/Q93k0oHOkVuIQB4vua2Ov0jcAdtcml5oV/TAznbfPCoYPt4nnphGDbIGOiyLzxF/O68TfzJX5qkhzjh6aYBQRRXDrgqt1tRe4IUGGu/SImbgJLh3l9KKWP9SbaoT/4pKGX0WsuGXJZZ3dKlx0WbCcMXLqfJGx0O8sL1iB1o5AiY3pDRdWRliT9982PeI2quuqGckgb0F9boyMntfueTOBXz0K+vSEXB/ipjpJG4EHE3dULj0ns9ACk2x8qrHf0XF+VVR24jlFaumPYvQjrw8ZKBJaPoC1BRbGDxyhCn5WxrFtZ7Un9UWCFdujhGfk8qVSpcyvzOgtmGMlJPZvSQy0pYzcYDLGgdF3rnsEqboR1EATQViAS+skZLS9FHsCglcSQFj1SUE4nbWbAVTd24AhTHMV2OAAM9gUyJ8Zq5MJzA4jkjWS1F17IlZzVXpcSAW6iA7HlQcAmsyNtJTnBg80lL9hYUnmcwwbhDrD4whbq2/1o6LcudLiSj40c+YYwHeklBryjQeFjPxRDDz4hyV9iHGpGgaS/ChZcgZRMLD9y8VsgU1imNVI1C2b1/hRqK+YUqZglsvTjlGVbi6jVtrfIHKIW0cIxzR9qOfs//wNA3iHz"))))