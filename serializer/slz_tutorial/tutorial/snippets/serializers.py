from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Snippet
    fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

  def create(self, validated_data):
    """
    Create and return a new `Snippet` instance, given the validated data.
    """
    return Snippet.objects.create(**validated_data)

  def update(self, instance, validated_data):

    instance.title = validated_data.get('title', instance.title)
    instance.code = validated_data.get('code', instance.code)
    instance.lineos = validated_data.get('lenos', instance.lenos)
    instance.language = validated_data.get('language', instance.language)
    instance.style = validated_data.get('style', instance.style)
    instance.save()
    return instance


""" 
The first part of the serializer class defines the fields that get serialized/deserialized.
The create() and update() methods define how fully fledged instances are created or modified
when calling serializer.save()

A serializer class is very similar to a Django Form class, and includes similar validation
flags on the various fields, such as required, max_length and default.

The field flags can also control how the serializer should be displayed in certain circumstances,
such as when rendering to HTML. The {'base_template': 'textarea.html'} flag above is equivalent to
using widget=widgets.Textarea on a Django Form class. This is particularly useful for controlling how
the browsable API should be displayed, as we'll see later in the tutorial.

We can actually also save ourselves some time by using the ModelSerializer class, as we'll see later,
but for now we'll keep our serializer definition explicit.

"""