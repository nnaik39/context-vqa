## Instructions for Downloading the Context-VQA Dataset

The images in the dataset are stored in the images.zip file. To download the questions and annotations, please download the dataset.json file.

The data is stored in this format. Here's an example:
```
    "images": [
        {
            "image_id": [IMAGE_ID],
            "question": "What's the weather like?",
            "context": "social_media",
            "annotations": [
                {
                    "answer1": "Partly sunny and cold",
                    "answer2": "Sunny, likely cold",
                    "answer3": "The picture is of a person holding a snowboard, in full winter gear, and on a snowy hill. So it's cold, but the sky doesn't have many clouds so it's also sunny."
                }
            ]
        }]
```

If you have any issues with downloading or using this dataset, please feel free to contact nanditan@cs.stanford.edu.
