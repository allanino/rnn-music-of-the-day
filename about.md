---
layout: page
title: About
permalink: /about/
---

Each day we post a music composed by a trained Recurrent Neural Network (RNN).

This is just for fun. I am not claiming this music to be superior or even equal in
quality to human produced music. I'm just amazed about how good the results are
given how simple the method is, so I wondered that some of you might find this cool.

The idea started some months ago, when Andrej Karpathy posted in his blog the
article [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/),
in which he talks about training a RNN to generate text a character at a time after being
trained on some dataset. In that article he shows some examples, including Shakespeare
like generated texts. He also released it's [code](https://github.com/karpathy/char-rnn).

Soon enough the Internet was flourishing with amazing things created using his code.
Some examples:

- Generating [Magic The Gathering cards](http://motherboard.vice.com/read/the-ai-that-learned-magic-the-gathering)
- Generating [Hearthstone cars](http://blizzardwatch.com/2015/07/15/neural-net-generates-hearthstone-cards-hilarity-results/)
- Generating [Obama's speechs](https://medium.com/@samim/obama-rnn-machine-generated-political-speeches-c8abd18a2ea0)
- Generating [Irish Folk music](https://www.reddit.com/r/MachineLearning/comments/36zi75/i_used_andrej_karpathys_charrnn_to_compose_irish/)
- Generating [Folk music](https://highnoongmt.wordpress.com/2015/05/22/lisls-stis-recurrent-neural-networks-for-folk-music-generation/)

The last two entries above are very similar to what I did, but I still think there is some merit
in my work, such as:

- I trained the network in much more data (8 MB versus 16 KB vs 415 KB) with greater musical variety.
- I synthesized the results in better sounding mp3 files.
- I'll be posting results daily here in this blog.

Let me give you some more details.

To train the network I started to look for ASCII notations for music and I found the
[abc notation](http://abcnotation.com/). It's a format much more suitable for training
the network than common MIDI representations, where each track is too far apart for the
network to correlate them. Another nice thing is that it supports chords and the chords
are also contiguous to the melody in the same bar. On the other hand, it's used
mainly by the folk music community, so the network was trained mainly with this kind of
music, but from many different sources and types, including traditional Irish,
Swiss, English, French and Chinese tunes. I collected a relatively huge amount
of music in this notation to allow the network to get more variety and better generalization.

I processed the results keeping only the valid files, valid here meaning without
errors or warnings being thrown by `abc2midi`. In this way I was able to generate
hundreds of musics which I will release here.

I'll release here (after some polishment) the scripts I used to collect and process the data as well as the
scripts I used to convert the results into actual sounds and sheet music. Hopefully anyone
will be able to reproduce my results.

Finally, I hope you enjoy this experiment's results as much as I do!
