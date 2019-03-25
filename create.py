from datetime import datetime, timedelta
from passlib.hash import pbkdf2_sha256 as sha256
from sqlalchemy.orm import sessionmaker

from connection import Base, engine
from models import User, Post, Tag, Comment

# Criar base de dados
Base.metadata.create_all(engine)

# Insert Test
user_admin = User(user='admin', password=sha256.hash('123456'))

tag_adipiscing = Tag(name='Adipiscing')
tag_gravida = Tag(name='Gravida')
tag_autor = Tag(name='Auctor')
tag_pharetra = Tag(name='Pharetra')
tag_lorem = Tag(name='Lorem')

comment_rhino = Comment(
    text='Rhinoceros, often abbreviated as rhino, is a group of five extant species of odd-toed ungulates in the family Rhinocerotidae.')

post_lorem = Post(text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris quis elit dui. Praesent ultricies hendrerit nulla, ut iaculis nibh efficitur ac. Phasellus facilisis pulvinar enim, ac venenatis nisi tincidunt imperdiet. Maecenas accumsan semper nulla eu tincidunt. Etiam sodales lectus enim, ac faucibus ex porttitor in. Nam euismod tempor eros sed eleifend. Ut sed molestie nibh, ac venenatis mauris. Etiam massa neque, posuere non justo et, dapibus consequat magna. Vivamus condimentum lectus in hendrerit porttitor. Vivamus a nibh arcu. In in elementum enim, eget condimentum arcu.',
                  tags=[tag_pharetra, tag_gravida, tag_lorem],
                  created_at=(datetime.utcnow() - timedelta(days=1)))
post_tempus = Post(text='Proin tempus, nisi at interdum sollicitudin, risus orci gravida metus, ut sagittis nisi sem vel felis. Nulla euismod ligula at tempus mollis. Phasellus vel luctus eros, a volutpat elit. Maecenas ut orci ipsum. Nullam et iaculis est. Cras rhoncus at dolor id ultricies. Donec a pretium ex. Sed id lacus egestas, blandit ipsum eget, ultricies nunc.',
                   tags=[tag_autor, tag_adipiscing])
post_proin = Post(text='Proin ex sem, mattis et varius in, auctor id lacus. Curabitur id est ultrices, aliquam nisl at, pellentesque eros. Etiam sed mollis dui, vitae lobortis ipsum. Nam in fermentum erat, vel accumsan mi. Suspendisse interdum dui sit amet orci molestie, at sollicitudin ex finibus. Mauris orci ligula, malesuada id ullamcorper id, gravida lacinia felis. Maecenas pulvinar, purus in laoreet luctus, velit felis gravida purus, dignissim hendrerit libero ipsum at augue. Morbi iaculis, tellus nec tincidunt maximus, ligula magna pretium risus, vitae tincidunt metus quam eu nisl.',
                  tags=[tag_pharetra])
post_etiam = Post(text='Etiam tempus libero semper, tincidunt sem id, aliquet massa. Ut a ipsum ipsum. Donec rhoncus vestibulum blandit. Nunc nec maximus nibh. Quisque eu semper quam. In auctor lorem ut diam commodo ullamcorper. Duis nec porttitor augue. Etiam est nisl, facilisis eget congue vitae, consectetur id nibh. Fusce enim ligula, ultrices non pulvinar elementum, maximus vel dui. Pellentesque congue, nunc lobortis efficitur euismod, nisl sapien convallis mauris, vel lobortis libero felis nec odio. Nullam viverra ultricies magna, vel sollicitudin mauris aliquet ac. Nam mollis magna sit amet varius finibus.',
                  tags=[tag_adipiscing],
                  comments=[comment_rhino])
post_phasellus = Post(text='Phasellus lorem felis, pharetra eget vestibulum non, pharetra quis tortor. Duis risus urna, commodo nec viverra eu, aliquam eget diam. Donec eget eros tincidunt, dignissim felis vel, vestibulum libero. Maecenas gravida leo arcu, in elementum dui interdum ac. Etiam egestas venenatis velit in iaculis. Praesent eleifend elementum sapien vitae lacinia. Duis gravida quam in semper luctus.',
                      tags=[tag_lorem],
                      comments=[comment_rhino])

# Commit Update
session = sessionmaker(bind=engine)()

session.add(user_admin)

session.add(tag_adipiscing)
session.add(tag_gravida)
session.add(tag_autor)
session.add(tag_pharetra)
session.add(tag_lorem)

session.add(comment_rhino)

session.add(post_lorem)
session.add(post_tempus)
session.add(post_proin)
session.add(post_etiam)
session.add(post_phasellus)

session.commit()
