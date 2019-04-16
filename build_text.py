#!/usr/bin/env python3

import fire
import json
import os
import numpy as np
import tensorflow as tf

import model
import sample
import encoder

def interact_model(
    model_name='117M',
    prompt = "",
    seed=None,
    nsamples=1,
    batch_size=None,
    length=270,
    temperature=1,
    top_k=40,
):
    print(prompt)
    if batch_size is None:
        batch_size = 1
    assert nsamples % batch_size == 0
    np.random.seed(seed)
    tf.set_random_seed(seed)

    enc = encoder.get_encoder(model_name)
    hparams = model.default_hparams()
    with open(os.path.join('models', model_name, 'hparams.json')) as f:
        hparams.override_from_dict(json.load(f))

    if length is None:
        length = hparams.n_ctx // 2
    elif length > hparams.n_ctx:
        raise ValueError(f"can't get samples longer than window size: {hparams.n_ctx}")

    with tf.Session(graph=tf.Graph()) as sess:
        context = tf.placeholder(tf.int32, [batch_size, None])
        output = sample.sample_sequence(
            hparams=hparams, length=length,
            context=context,
            batch_size=batch_size,
            temperature=temperature, top_k=top_k
        )[:, 1:]

        saver = tf.train.Saver()
        ckpt = tf.train.latest_checkpoint(os.path.join('models', model_name))
        saver.restore(sess, ckpt)

        raw_text = prompt
        context_tokens = enc.encode(raw_text)
        generated = 0
        for _ in range(nsamples // batch_size):
            out = sess.run(output, feed_dict={
                context: [context_tokens for _ in range(batch_size)]
            })
            for i in range(batch_size):
                generated += 1
                text = enc.decode(out[i])
                print("=" * 40 + " MESSAGE " + str(generated) + " " + "=" * 40)
                print(f"{text}")
                gpt_text = text
        print("=" * 80)
        return gpt_text

if __name__ == '__main__':
    gpt_text = fire.Fire(interact_model)

