from datetime import timedelta

import bcrypt
import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

import models
from db_conf import db_session
from jwt_token import create_access_token
from schemas import PostModel, PostSchema, UserSchema

db = db_session.session_factory()

app = FastAPI()


class Query(graphene.ObjectType):

    all_posts = graphene.List(PostModel)
    post_by_id = graphene.Field(PostModel, post_id=graphene.Int(required=True))

    def resolve_all_posts(self, info):
        query = PostModel.get_query(info)
        return query.all()

    def resolve_post_by_id(self, info, post_id):
        return db.query(models.Post).filter(models.Post.id == post_id).first()


class AuthenticateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    ok = graphene.Boolean()
    token = graphene.String()

    @staticmethod
    def mutate(root, info, username, password):
        user = UserSchema(username=username, password=password)

        db_user_info = (
            db.query(models.User).filter(models.User.username == username).first()
        )

        if bcrypt.checkpw(
            user.password.encode("utf-8"), db_user_info.password.encode("utf-8")
        ):
            access_token_expires = timedelta(minutes=60)
            access_token = create_access_token(
                data={"user": username}, expires_delta=access_token_expires
            )
            ok = True
            return AuthenticateUser(ok=ok, token=access_token)

        else:
            ok = False
            return AuthenticateUser(ok=ok)


class CreateNewUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, username, password):

        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        password_hash = hashed_password.decode("utf8")

        user = UserSchema(username=username, password=password_hash)
        db_user = models.User(username=user.username, password=password_hash)
        db.add(db_user)

        try:
            db.commit()
            db.refresh(db_user)
            ok = True
            return CreateNewUser(ok=ok)
        except:
            db.rollback()
            raise

        db.close()


class CreateNewPost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, title, content):
        post = PostSchema(title=title, content=content)
        db_post = models.Post(title=post.title, content=post.content)
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        ok = True
        return CreateNewPost(ok=ok)


class PostMutations(graphene.ObjectType):
    authenticate_user = AuthenticateUser.Field()
    create_new_post = CreateNewPost.Field()
    create_new_user = CreateNewUser.Field()


app.add_route(
    "/graphql", GraphQLApp(schema=graphene.Schema(query=Query, mutation=PostMutations))
)
