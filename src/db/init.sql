create table grocery_app.grocery(
  item_id VARCHAR(32),
  name VARCHAR(45) NOT NULL,
  price VARCHAR(45) NOT NULL,
  quantity VARCHAR(45) NOT NULL,
  PRIMARY KEY (item_id));



create table grocery_app.order_item(
  order_id VARCHAR(32),
  item_id VARCHAR(32) NOT NULL,
  quantity VARCHAR(32) NOT NULL,
  PRIMARY KEY (order_id, item_id),
  foreign key (item_id) references grocery_app.grocery(item_id)
  );

create table grocery_app.user_order(
  user_id VARCHAR(32),
  order_id VARCHAR(32),
 PRIMARY KEY (user_id, order_id),
  foreign key (user_id) references grocery_app.user(user_id)


  );


  create table grocery_app.user(
  user_id VARCHAR(32),
  user_name VARCHAR(32),

  PRIMARY KEY (user_id),

  );

INSERT INTO grocery_app."user" (user_id,user_name) VALUES ('USR-00001', 'Ram');
INSERT INTO grocery_app."user" (user_id,user_name) VALUES ('USR-00002', 'Shyam');
