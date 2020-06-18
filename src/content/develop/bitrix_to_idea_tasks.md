Title: Настраиваем задачи из bitrix24 в jetbrains idea
Date: 2020-06-18 11:40
Author: ifilatov
Tags: idea, howto, bitrix24, tasks
Image: /media/b24_to_idea_tasks.png
Status: published
Summary: Если вы пишете код в idea, а ваш клиент или работодатель ставит задачи в bitrix24, то пользуясь инструкцией в данной статье вы сможете использовать информацию из задачь прямо в idea

> оригинал [здесь](https://habr.com/ru/post/427451/), мои правки ниже

## Переменные

```ini
bitrix_url:     url вашего портала [sysadmin.bitrix24.ru]
group_id:       имя группы [1]
user_id:        id вашего пользователя [1] (админ обычно №1)
web_hook_key:   ключ входящего вебхука
```

## JSON URL

```cfg
# Все открытые задачи
Task List URL: https://{bitrix_url}/rest/{user_id}/{web_hook_key}/task.item.list.json?ORDER[]=&FILTER[RESPONSIBLE_ID]={user_id}}&FILTER[%3CREAL_STATUS]=4&PARAMS[]=&SELECT[]=*

# Все открытые задачи только из определенной группы
Single Task URL: https://{bitrix_url}/rest/{user_id}/{web_hook_key}/task.item.list.json?ORDER[]=&FILTER[RESPONSIBLE_ID]={user_id}}&FILTER[%3CREAL_STATUS]=4&PARAMS[]=&SELECT[]=*&FILTER[GROUP_ID]={group_id}
```

## Сопоставление полей

```ini
tasks                  | result[*]
id                     | ID
summary                | TITLE
description            | DESCRIPTION
updated                | CHANGED_DATE
created                | CREATED_DATE
singleTask-id          | result.ID
singleTask-summary     | result.TITLE
singleTask-description | result.DESCRIPTION
singleTask-updated     | result.CHANGED_DATE
singleTask-created     | result.CREATED_DATE
```

![Сопоставление полей](https://hsto.org/webt/re/9e/b7/re9eb7r1mgu0crwpkapyvjovaea.png)