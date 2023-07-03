import React, { useEffect, useRef } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchMessages, addMessage, selectMessages } from '../features/chatSlice';

const Chat = () => {
  const dispatch = useDispatch();
  const messages = useSelector(selectMessages);
  const messageInputRef = useRef();
  console.log(messages)

  useEffect(() => {
    dispatch(fetchMessages());
  }, [dispatch]);

  const handleSend = () => {
    const text = messageInputRef.current.value.trim();
    if (text) {
      dispatch(addMessage(text));
      messageInputRef.current.value = '';
    }
  };

  return (
    <div>
      <ul>
        {messages.map(message => (
          <li key={message.id}>
            <span>{message.text}</span>
            <span>{message.created_at}</span>
          </li>
        ))}
      </ul>
      <div>
        <input type="text" ref={messageInputRef} />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
};

export default Chat;
