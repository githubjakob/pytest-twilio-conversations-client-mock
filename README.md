# Twilio Conversations Client Mock

Current status: Under development as a hobby project.

Works for the most basic operations, e.g. `conversations.create()` or `conversations(sid).fetch()`.
Currently many operations, fields or error cases are not implemented. (See the [tests](https://github.com/githubjakob/pytest-twilio-conversations-client-mock/tests/README.md))

## Usage

```
pip install pytest-twilio-conversations-client-mock
```

Mock the Twilio Client in your tests:

```
patch("twilio.rest.Client", return_value=ClientMock()).start()
```

More see [example](https://github.com/githubjakob/pytest-twilio-conversations-client-mock/example/README.md).
