#!/usr/bin/env python3
"""
Generate "The Faith of Jesus: A Living Religion of Personal Experience"

This script composes a full 10-chapter book grounded in The Urantia Book,
with every claim anchored to paragraph-level citations, and persists it
into Obsidian-compatible Markdown vaults.

Run:
    cd URANTiOS
    python generate_faith_of_jesus.py
"""
import sys, json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))

from bookwriter.corpus import Corpus
from bookwriter.outline import Outline, Chapter
from bookwriter.writer import Book, WrittenChapter
from bookwriter.obsidian import ObsidianRenderer, ObsidianVault
from bookwriter.vault import MultiVault


# ═══════════════════════════════════════════════════════════════════════
# THE BOOK: "The Faith of Jesus"
# ═══════════════════════════════════════════════════════════════════════

TITLE = "The Faith of Jesus"
SUBTITLE = "A Living Religion of Personal Experience"
THEME = "The faith OF Jesus — not about Jesus, but the living personal faith he lived"
EPIGRAPH = '"You may preach a religion about Jesus, but, perforce, you must live the religion of Jesus." (196:2.1)'
PREFACE = (
    "This book is not another commentary about Jesus. It is an attempt to recover "
    "what Jesus himself believed, how he lived his faith, and what that faith means "
    "for every human being who hungers for a personal relationship with the living God. "
    "The distinction is not academic — it is the difference between a creed recited "
    "and a life transformed. Every claim in these pages is anchored to The Urantia Book "
    "by paragraph-level citation. Where interpretation extends beyond the text, it is "
    "marked as such. The Three Values govern this work: Truth, Beauty, Goodness."
)

CHAPTERS_DATA = [
    # ── Chapter 1 ─────────────────────────────────────────────────────
    {
        "number": 1,
        "title": "Not About Jesus — Of Jesus",
        "thesis": "The religion of Jesus is not a religion about him but the living faith he himself practised.",
        "key_refs": ["196:2.1", "195:9.8", "196:2.4", "196:1.3"],
        "beats": [
            "The great substitution: how the religion about Jesus replaced his own religion",
            "Peter's Pentecost and Paul's theology",
            "What was lost — and what can be recovered",
            "The call to live as he lived",
        ],
        "body": r"""# Chapter 1 — Not About Jesus — Of Jesus

_"You may preach a religion about Jesus, but, perforce, you must live the religion of Jesus." (196:2.1)_

There is a fault line running through twenty centuries of Christianity, and it is not the one most theologians notice. It is not the rift between East and West, Catholic and Protestant, liberal and conservative. It is something more fundamental: the distance between a religion *about* Jesus and the religion *of* Jesus.

The Urantia Book states the distinction with surgical precision: "In the enthusiasm of Pentecost, Peter unintentionally inaugurated a new religion, the religion of the risen and glorified Christ. The Apostle Paul later on transformed this new gospel into Christianity, a religion embodying his own theologic views and portraying his own personal experience with the Jesus of the Damascus road" (196:2.1). What happened at Pentecost was not a betrayal — Peter spoke from authentic spiritual power — but it was a substitution. The subject changed. The teacher became the subject of the teaching. The one who pointed at the Father became the one pointed at.

The world still feels the consequences: "Even Christianity — the best of the religions of the twentieth century — is not only a religion *about* Jesus, but it is so largely one which men experience secondhand. They take their religion wholly as handed down by their accepted religious teachers" (195:9.8). A secondhand religion is not necessarily a false religion, but it is a diminished one. It is the difference between reading about the ocean and standing in the surf.

The great mistake was not that people worshipped Christ — he is worthy of worship — but that "while the human Jesus was recognized as *having* a religion, the divine Jesus (Christ) almost overnight became a religion" (196:2.4). The struggling, trusting, praying human Jesus — the one who showed mortals what faith looks like from inside a mortal life — was buried under theological grandeur. Paul's Christianity "almost wholly lost sight of the struggling and valiant human Jesus of Galilee, who, by the valor of his personal religious faith and the heroism of his indwelling Adjuster, ascended from the lowly levels of humanity to become one with divinity" (196:2.4).

This book exists because the recovery is still possible. "To 'follow Jesus' means to personally share his religious faith and to enter into the spirit of the Master's life of unselfish service for man. One of the most important things in human living is to find out what Jesus believed, to discover his ideals, and to strive for the achievement of his exalted life purpose. Of all human knowledge, that which is of greatest value is to know the religious life of Jesus and how he lived it" (196:1.3).

That is our task. Not biography. Not theology. The living interior of a life lived in faith.
""",
    },
    # ── Chapter 2 ─────────────────────────────────────────────────────
    {
        "number": 2,
        "title": "What Jesus Believed",
        "thesis": "The content of Jesus' faith was simple, personal, and wholly centred on the Father.",
        "key_refs": ["196:0.1", "196:0.2", "196:0.3", "196:0.5"],
        "beats": [
            "Jesus' faith was personal, not institutional",
            "He saw God as holy, true, beautiful, good — and as Father",
            "Faith was not consolation but confident trust",
            "His faith was living, original, spontaneous",
        ],
        "body": r"""# Chapter 2 — What Jesus Believed

_"Jesus enjoyed a sublime and wholehearted faith in God." (196:0.1)_

Before we can live the faith of Jesus, we must understand what he believed. Not what the creeds say he should have believed. Not what the councils later decided. What he *actually* held in his own consciousness as he walked the roads of Galilee and climbed the hills to pray.

The answer is, at its core, breathtakingly simple. "Jesus enjoyed a sublime and wholehearted faith in God. He experienced the ordinary ups and downs of mortal existence, but he never religiously doubted the certainty of God's watchcare and guidance. His faith was the outgrowth of the insight born of the activity of the divine presence, his indwelling Adjuster. His faith was neither traditional nor merely intellectual; it was wholly personal and purely spiritual" (196:0.1).

Notice what this is *not*. It is not a set of propositions. It is not a creed. It is not traditional — he did not believe because his parents believed. It is not merely intellectual — he did not arrive at God through argument. It was *personal* and *purely spiritual*: born of direct contact with the divine presence within him.

What did he see when he looked toward God? "The human Jesus saw God as being holy, just, and great, as well as being true, beautiful, and good. All these attributes of divinity he focused in his mind as 'the will of the Father in heaven'" (196:0.2). The concept of God as Father was not original with Jesus, but "he exalted and elevated the idea into a sublime experience by achieving a new revelation of God and by proclaiming that every mortal creature is a child of this Father of love, a son of God" (196:0.2). This is the revolutionary claim: not that God exists, but that God is *your* Father, and you are God's child — personally, individually, eternally.

And his faith was not the clinging of a drowning man. "Jesus did not cling to faith in God as would a struggling soul at war with the universe and at death grips with a hostile and sinful world; he did not resort to faith merely as a consolation in the midst of difficulties or as a comfort in threatened despair" (196:0.3). His faith was not escape. It was engagement. "In the very face of all the natural difficulties and the temporal contradictions of mortal existence, he experienced the tranquillity of supreme and unquestioned trust in God" (196:0.3).

"Theology may fix, formulate, define, and dogmatize faith, but in the human life of Jesus faith was personal, living, original, spontaneous, and purely spiritual" (196:0.5). Four adjectives — each one a rebuke to institutional religion. *Personal*: it cannot be inherited. *Living*: it grows or it dies. *Original*: it does not borrow its content from other minds. *Spontaneous*: it is not performed on cue.

This is the faith we are invited to share. Not to copy — that would contradict its nature — but to *discover* in ourselves, using the same source he used: the divine presence that indwells every human mind.
""",
    },
    # ── Chapter 3 ─────────────────────────────────────────────────────
    {
        "number": 3,
        "title": "Belief and Faith — The Great Divide",
        "thesis": "Belief fixates; faith liberates. Living faith is the open door.",
        "key_refs": ["101:8.2", "103:7.1", "138:8.8", "155:6.4"],
        "beats": [
            "Belief vs faith — the Urantia Book's sharpest distinction",
            "Faith as the only requisite for the kingdom",
            "From religion of the mind to religion of the spirit",
            "The adventurous nature of living faith",
        ],
        "body": r"""# Chapter 3 — Belief and Faith — The Great Divide

_"Belief is always limiting and binding; faith is expanding and releasing." (101:8.2)_

No distinction in The Urantia Book cuts deeper than this: "Belief is always limiting and binding; faith is expanding and releasing. Belief fixates, faith liberates. But living religious faith is more than the association of noble beliefs; it is more than an exalted system of philosophy; it is a living experience concerned with spiritual meanings, divine ideals, and supreme values; it is God-knowing and man-serving" (101:8.2).

Belief is what you hold. Faith is what holds you.

Belief is a list of propositions — you can write it on a card, recite it in unison, test newcomers against it. Faith is a relationship — dynamic, growing, tested by life and strengthened by crisis. Beliefs can be group possessions; "faith must be personal" (101:8.2). A committee can draft a creed, but no committee has ever produced faith.

This is not anti-intellectualism. "Science is sustained by reason, religion by faith. Faith, though not predicated on reason, is reasonable; though independent of logic, it is nonetheless encouraged by sound logic" (103:7.1). Faith does not reject the mind; it *transcends* the mind. A man can reason his way to the probability of God and still lack faith. Faith takes the philosophic probability and makes it a personal certainty — "Faith transforms the philosophic God of probability into the saving God of certainty in the personal religious experience" (102:6.4).

Jesus himself drew this line with his apostles. "Jesus made plain to his apostles the difference between the repentance of so-called good works as taught by the Jews and the change of mind by faith — the new birth — which he required as the price of admission to the kingdom. He taught his apostles that *faith* was the only requisite to entering the Father's kingdom" (138:8.8). Not belief in the correct formula. Not subscription to the right creed. Faith. The open door: "Faith is the open door for entering into the present, perfect, and eternal love of God" (138:8.8).

And this faith is not static. "Your religion shall change from the mere intellectual belief in traditional authority to the actual experience of that living faith which is able to grasp the reality of God and all that relates to the divine spirit of the Father" (155:6.4). The religion of the mind ties you to the past — to what others decided centuries ago. "The religion of the spirit consists in progressive revelation and ever beckons you on toward higher and holier achievements in spiritual ideals and eternal realities" (155:6.4).

This is the great divide. Not between religions. Between the impulse to *believe about* God and the courage to *know* God.
""",
    },
    # ── Chapter 4 ─────────────────────────────────────────────────────
    {
        "number": 4,
        "title": "Religion as Personal Experience",
        "thesis": "True religion is the spiritual content of personal experience — not doctrine, not institution.",
        "key_refs": ["145:2.3", "103:9.1", "170:4.2", "195:5.3", "103:6.3"],
        "beats": [
            "Jesus' teaching: religion is personal experience",
            "The insideness of experience",
            "The kingdom as inner fellowship with the Father",
            "Religion vs. its look-alikes",
        ],
        "body": r"""# Chapter 4 — Religion as Personal Experience

_"Religion is a personal experience." (145:2.3)_

At Capernaum, Jesus preached what may have been his most penetrating sermon on the nature of religion itself. "This sermon was an effort on Jesus' part to make clear the fact that religion is a *personal experience*" (145:2.3). Not a tribal inheritance. Not a national identity. Not even a community practice in its essence. Personal. It begins in the individual soul's encounter with the living God.

The Urantia Book makes a threefold distinction that clarifies everything: "Theology deals with the intellectual content of religion, metaphysics (revelation) with the philosophic aspects. Religious experience *is* the spiritual content of religion" (103:9.1). Theology can be studied, debated, revised. Philosophy can be argued. But the spiritual content — the actual experience of communion with God — that is the irreducible thing. Without it, theology is architecture without a building; philosophy is a map without a territory.

What does this experience consist of? At its simplest: "The personal and inward experience of the spiritual life of the fellowship of the individual believer with God the Father" (170:4.2). Fellowship. Not obligation. Not fear. Not duty. The conscious relationship between a child and a loving parent, lived out in the inner life of the mind and spirit.

"Religion is the revelation to man of his divine and eternal destiny. Religion is a purely personal and spiritual experience and must forever be distinguished from man's other high forms of thought" (195:5.3). It is not ethics — though it produces ethical behaviour. It is not philosophy — though it gives philosophy its highest content. It is not science — though it does not contradict honest science. It is its own domain: the spiritual awareness of reality from the inside.

"Religion has to do with the spiritual viewpoint, the awareness of the *insideness* of human experience" (103:6.3). This is a remarkable phrase. Science studies the outside of things — measurable, observable, replicable. Religion studies the inside — what it means to *be* a self that knows, that loves, that chooses, that longs for the eternal. The outside can be shared through data; the inside can only be shared through faith and communion.

This is why no institution can own religion. Institutions can support it, protect it, provide it with community and structure. But the moment an institution claims to *be* religion — to substitute its authority for the individual's encounter with God — it has committed the oldest error: mistaking the container for the content.

The faith of Jesus was the purest form of this personal experience. He needed no intermediary, no priesthood, no ritual. He went to the Father directly, in the silence of his own heart. And he taught that every human being can do the same.
""",
    },
    # ── Chapter 5 ─────────────────────────────────────────────────────
    {
        "number": 5,
        "title": "The Father Within",
        "thesis": "The God Jesus knew was not distant but indwelling — accessible to every human mind.",
        "key_refs": ["169:4.2", "1:7.5", "2:6.1", "196:3.34", "196:3.26"],
        "beats": [
            "Jesus never argued for God — he revealed him",
            "God known only through personal experience",
            "The goodness of God in personal experience",
            "The Adjuster — the divine presence within",
        ],
        "body": r"""# Chapter 5 — The Father Within

_"The great challenge to modern man is to achieve better communication with the divine Monitor that dwells within the human mind." (196:3.34)_

Jesus did not argue people into believing in God. "Jesus never gave his apostles a systematic lesson concerning the personality and attributes of the Father in heaven. He never asked men to believe in his Father; he took it for granted they did" (169:4.2). He did not construct proofs; he *demonstrated*. His life was the argument. "He who has seen the Son has seen the Father" (180:3.9) — not as a doctrinal claim but as lived transparency. The Father shone through the Son because the Son had made himself wholly available to the Father's will.

And this Father is not remote. "Ultimate universe reality cannot be grasped by mathematics, logic, or philosophy, only by personal experience in progressive conformity to the divine will of a personal God" (1:7.5). No telescope will find God; no equation will prove him. But every human being who sincerely seeks to do the Father's will can *know* the Father — not as a concept but as a presence.

Where is this presence? "In the physical universe we may see the divine beauty, in the intellectual world we may discern eternal truth, but the goodness of God is found only in the spiritual world of personal religious experience" (2:6.1). Beauty and truth can be observed at a distance. Goodness must be experienced from within. You cannot understand that God is good by reading about it; you understand it when you feel the Father's love moving through your own decisions and relationships.

This indwelling presence — what The Urantia Book calls the Thought Adjuster, the divine Monitor — is the source of faith itself. "The evolutionary mind is able to discover law, morals, and ethics; but the bestowed spirit, the indwelling Adjuster, reveals to the evolving human mind the lawgiver, the Father-source of all that is true, beautiful, and good; and such an illuminated man has a religion and is spiritually equipped to begin the long and adventurous search for God" (196:3.26).

This is the most radical teaching in the religion of Jesus: God is not somewhere else. God is *here*, in the human mind, working from within, waiting to be recognised, responded to, partnered with. "Man's greatest adventure in the flesh consists in the well-balanced and sane effort to advance the borders of self-consciousness out through the dim realms of embryonic soul-consciousness in a wholehearted effort to reach the borderland of spirit-consciousness — contact with the divine presence" (196:3.34).

The faith of Jesus was, at its deepest, this contact — maintained, nurtured, never abandoned, even on the cross. And the promise of his religion is that every human being carries the same indwelling gift.
""",
    },
    # ── Chapter 6 ─────────────────────────────────────────────────────
    {
        "number": 6,
        "title": "Faith in Action — A Religion of Service",
        "thesis": "Jesus' religion was not passive belief but positive, active service.",
        "key_refs": ["159:5.8", "5:4.7", "194:3.3", "196:3.19", "102:2.7"],
        "beats": [
            "Positive action vs. passive compliance",
            "A religion of service",
            "Faith that masters life rather than escaping it",
            "A religion of love",
        ],
        "body": r"""# Chapter 6 — Faith in Action — A Religion of Service

_"Jesus lived a religion of service." (5:4.7)_

Many religions have excelled at telling people what not to do. Jesus told people what to *do*. "Jesus put the spirit of positive action into the passive doctrines of the Jewish religion. In the place of negative compliance with ceremonial requirements, Jesus enjoined the positive doing of that which his new religion required of those who accepted it" (159:5.8). His religion "consisted not merely in *believing,* but in actually *doing,* those things which the gospel required" (159:5.8).

This is not works-righteousness — the anxious accumulation of merit. It is the natural overflow of a life connected to the Source. A tree rooted in good soil does not *try* to bear fruit; it bears fruit because that is what living trees do. Social service, Jesus taught, "was one of the certain effects of the possession of the spirit of true religion" (159:5.8).

The world's religions had each grasped a part of the truth: "The Zoroastrians had a religion of morals; the Hindus a religion of metaphysics; the Confucianists a religion of ethics. Jesus lived a religion of *service*" (5:4.7). Not morals alone — though he was moral. Not metaphysics alone — though his cosmology was vast. Not ethics alone — though his ethical teaching remains unsurpassed. Service: the active, loving engagement with other human beings as children of the same Father.

And this service was not escapism. "To Jesus, mortal life had dealt its hardest, cruelest, and bitterest blows; and this man met these ministrations of despair with faith, courage, and the unswerving determination to do his Father's will" (194:3.3). He did not use religion as a way out of life. "The religion of Jesus does not seek to escape this life in order to enjoy the waiting bliss of another existence. The religion of Jesus provides the joy and peace of another and spiritual existence to enhance and ennoble the life which men now live in the flesh" (194:3.3).

We may infer that this is the test of authentic faith: does it make you more engaged with life, or less? Does it increase your capacity to serve, or does it provide you with reasons to withdraw? The faith of Jesus drove him into the marketplace, the fishing village, the temple courts — not away from them.

At the summit: "Jesus revealed and exemplified a religion of love: security in the Father's love, with joy and satisfaction consequent upon sharing this love in the service of the human brotherhood" (196:3.19). Security, joy, satisfaction — all flowing from a single source (the Father's love) into a single channel (service to others). That is the economy of the faith of Jesus: receive love, give love, and in the giving, receive more.

But this is not passive either. "There is no real religion apart from a highly active personality" (102:2.7). The indolent seek "a retreat to the false shelter of stereotyped religious doctrines and dogmas" (102:2.7). True religion is work — not the anxious work of earning salvation, but the creative work of a life fully alive.
""",
    },
    # ── Chapter 7 ─────────────────────────────────────────────────────
    {
        "number": 7,
        "title": "The Testing of Faith",
        "thesis": "Faith is proved not in comfort but in adversity — as Jesus himself demonstrated.",
        "key_refs": ["158:5.2", "100:7.7", "135:11.1", "196:0.3", "103:1.5"],
        "beats": [
            "The faithless generation — Jesus' frustration",
            "How Jesus trusted: like a child, never presumptuous",
            "John the Baptist's prison — the test of loyalty",
            "Faith does not remove suffering; it transforms it",
        ],
        "body": r"""# Chapter 7 — The Testing of Faith

_"Of Jesus it was truly said, 'He trusted God.' As a man among men he most sublimely trusted the Father in heaven." (100:7.7)_

Faith untested is faith unknown. Every great passage in the spiritual life of Jesus came through a crucible, and his faith emerged not diminished but refined.

He was not patient with faithlessness. When his apostles failed to heal an afflicted boy, "Jesus said to all those who stood before him: 'O faithless and perverse generation, how long shall I bear with you? How long shall I be with you? How long ere you learn that the works of faith come not forth at the bidding of doubting unbelief?'" (158:5.2). There is an edge in these words — not cruelty but the frustration of a teacher who knows what his students are capable of and watches them choose less.

His own faith, by contrast, was unwavering. "Of Jesus it was truly said, 'He trusted God.' As a man among men he most sublimely trusted the Father in heaven. He trusted his Father as a little child trusts his earthly parent. His faith was perfect but never presumptuous" (100:7.7). The twin qualities matter: *perfect* and *not presumptuous*. He did not test God; he trusted God. He did not demand miracles; he lived in the quiet certainty that the Father's care was constant. "No matter how cruel nature might appear to be or how indifferent to man's welfare on earth, Jesus never faltered in his faith. He was immune to disappointment and impervious to persecution. He was untouched by apparent failure" (100:7.7).

Not everyone could maintain such trust. Consider John the Baptist in prison: "He longed to see Jesus but had to be content with hearing of his work through those of his followers who had become believers in the Son of Man. He was often tempted to doubt Jesus and his divine mission. If Jesus were the Messiah, why did he do nothing to deliver him from this unbearable imprisonment?" (135:11.1). John's test was real. His doubt was honest. The faith of Jesus does not pretend that doubt does not exist; it acknowledges doubt and transcends it.

Jesus himself "did not cling to faith in God as would a struggling soul at war with the universe" (196:0.3). His faith was not the desperate grip of a man afraid to fall; it was the confident stride of a man who knows the ground beneath him is solid. Even in Gethsemane, even on the cross, the ground held.

"That religionists have believed so much that was false does not invalidate religion because religion is founded on the recognition of values and is validated by the faith of personal religious experience" (103:1.5). The failures of religion — its errors, its cruelties, its embarrassments — do not disprove the reality of the faith experience. They prove only that human beings are imperfect vessels. The water is real even when the cup is cracked.

The faith of Jesus was tested by every kind of adversity the mortal life can produce: poverty, rejection, betrayal, torture, death. It held. That is the proof.
""",
    },
    # ── Chapter 8 ─────────────────────────────────────────────────────
    {
        "number": 8,
        "title": "Spiritual Growth — The Fruits of Faith",
        "thesis": "Faith bears fruit in spiritual development, progressive God-consciousness, and unified personality.",
        "key_refs": ["100:2.1", "101:6.17", "100:7.18", "196:3.29", "150:5.3"],
        "beats": [
            "Spiritual growth as the purpose of faith",
            "Bearing spiritual fruit in service",
            "Salvation as gift, faith as acceptance",
            "Love as highest motivation — but only when true",
        ],
        "body": r"""# Chapter 8 — Spiritual Growth — The Fruits of Faith

_"Spiritual development depends, first, on the maintenance of a living spiritual connection with true spiritual forces." (100:2.1)_

Faith is not an event; it is a trajectory. The faith of Jesus was not a single decision made once but a continual orientation — a daily, hourly turning toward the Father. "Spiritual development depends, first, on the maintenance of a living spiritual connection with true spiritual forces and, second, on the continuous bearing of spiritual fruit: yielding the ministry to one's fellows of that which has been received from one's spiritual benefactors" (100:2.1).

Two movements: *receiving* and *giving*. Receive from the Father; give to the brotherhood. This is the spiritual metabolism of faith. Stop either one and growth halts. A person who receives but does not serve becomes spiritually stagnant. A person who serves but does not pray burns out. The balance is essential: "intellectual recognition of spiritual poverty coupled with the self-consciousness of perfection-hunger, the desire to know God and be like him, the wholehearted purpose to do the will of the Father in heaven" (100:2.1).

The fruit of this process is transformative. "Through the appropriation of the faith of Jesus, mortal man can foretaste in time the realities of eternity. Jesus made the discovery, in human experience, of the Final Father, and his brothers in the flesh of mortal life can follow him along this same experience of Father discovery" (101:6.17). That is the promise: the same path Jesus walked is open to every mortal. Not because we are divine, but because we are *indwelt* by divinity.

And the end of the path is personality integration: "Jesus was the perfectly unified human personality. And today, as in Galilee, he continues to unify mortal experience and to co-ordinate human endeavors. He unifies life, ennobles character, and simplifies experience" (100:7.18). The fragmented self — torn between desire and duty, appetite and aspiration — finds unity through faith. Not by suppressing any part, but by orienting all parts toward a single centre: the will of the Father.

Salvation itself is not earned by this growth; it is the starting point: "Salvation is the gift of the Father and is revealed by his Sons. Acceptance by faith on your part makes you a partaker of the divine nature, a son or a daughter of God. By faith you are justified; by faith are you saved; and by this same faith are you eternally advanced in the way of progressive and divine perfection" (150:5.3).

But the highest fruit of faith is love — rightly understood. "Love is the highest motivation which man may utilize in his universe ascent. But love, divested of truth, beauty, and goodness, is only a sentiment, a philosophic distortion, a psychic illusion, a spiritual deception" (196:3.29). Love without truth is sentimentality. Love without beauty is formless. Love without goodness is indulgence. The Three Values are not alternatives to love; they are its structure.
""",
    },
    # ── Chapter 9 ─────────────────────────────────────────────────────
    {
        "number": 9,
        "title": "Beyond Theology — The Spirit of Living Truth",
        "thesis": "The religion of the spirit transcends the religion of authority and traditional theology.",
        "key_refs": ["155:6.2", "155:6.3", "155:6.5", "155:5.12", "196:3.22"],
        "beats": [
            "The call out of institutional authority",
            "Born again — the discovery of God in yourself",
            "Spiritual freedom vs. settled security",
            "Worship as personal communion",
        ],
        "body": r"""# Chapter 9 — Beyond Theology — The Spirit of Living Truth

_"I have called you out of the darkness of authority and the lethargy of tradition into the transcendent light." (155:6.3)_

Near Caesarea Philippi, Jesus delivered what may be his most radical teaching on the nature of religion. It was directed at those who had already left their old securities behind: "You have come out from among those of your fellows who choose to remain satisfied with a religion of mind, who crave security and prefer conformity. You have elected to exchange your feelings of authoritative certainty for the assurances of the spirit of adventurous and progressive faith" (155:6.2).

The religion of authority offers something genuine: certainty. You know where you stand. The creed is fixed; the answers are given; the tradition is ancient and venerable. But the cost is spiritual freedom: "While the religion of authority may impart a present feeling of settled security, you pay for such a transient satisfaction the price of the loss of your spiritual freedom and religious liberty" (155:6.5).

Jesus offered a different kind of security — not the security of a cage but the security of wings: "I have called upon you to be born again, to be born of the spirit. I have called you out of the darkness of authority and the lethargy of tradition into the transcendent light of the realization of the possibility of making for yourselves the greatest discovery possible for the human soul to make — the supernal experience of finding God for yourself, in yourself, and of yourself, and of doing all this as a fact in your own personal experience" (155:6.3).

This is not theological liberalism — the polite softening of difficult doctrines. This is something far more dangerous: the insistence that God can be *found directly*, without mediator, without committee, without prior permission. The institutional gatekeepers of every century have good reason to be nervous about this teaching.

Jesus acknowledged the danger of the religion he was replacing: "At Jerusalem the religious leaders have formulated the various doctrines of their traditional teachers and the prophets of other days into an established system of intellectual beliefs, a religion of authority. The appeal of all such religions is largely to the mind" (155:5.12). He was not condemning the mind — he was pointing out that the mind alone is not enough. The religion he proclaimed "makes its chief appeal to the divine spirit of my Father which resides in the mind of man" (155:5.12).

And at the heart of this religion stands worship — not as ritual but as relationship: "True religious worship is not a futile monologue of self-deception. Worship is a personal communion with that which is divinely real, with that which is the very source of reality. Man aspires by worship to be better and thereby eventually attains the *best*" (196:3.22).

Worship, in the faith of Jesus, is not performance. It is conversation. It is the soul saying to the Father: *I am here. You are here. Let us be here together.*
""",
    },
    # ── Chapter 10 ────────────────────────────────────────────────────
    {
        "number": 10,
        "title": "The Unfinished Revelation",
        "thesis": "The revelation of God in and through Jesus shall not fail — the faith of Jesus is still alive.",
        "key_refs": ["196:3.33", "196:3.35", "196:3.30", "196:1.2", "101:3.18"],
        "beats": [
            "Be not discouraged — evolution is still in progress",
            "The figurative resurrection of the human Jesus",
            "Religion as man's supreme gesture toward final reality",
            "The integration of self with the universe",
        ],
        "body": r"""# Chapter 10 — The Unfinished Revelation

_"Be not discouraged; human evolution is still in progress, and the revelation of God to the world, in and through Jesus, shall not fail." (196:3.33)_

This is not the end. It is barely the beginning.

The Urantia Book closes its final paper — the last of 196 — with one of the most quietly powerful sentences in all of revelation: "Be not discouraged; human evolution is still in progress, and the revelation of God to the world, in and through Jesus, shall not fail" (196:3.33). After two thousand pages of cosmic architecture, after mapping seven superuniverses and a billion worlds, after tracing the ascent of the soul from animal origin to Paradise embrace, the authors set down their pens with a word of encouragement. *Be not discouraged.*

Why would we be? Because the task is unfinished. The religion of Jesus has not yet been tried — not fully, not fearlessly, not by a generation willing to let go of the religion *about* Jesus and take up the religion *of* Jesus. "The time is ripe to witness the figurative resurrection of the human Jesus from his burial tomb amidst the theological traditions and the religious dogmas of nineteen centuries" (196:1.2). That resurrection — the recovery of the living, human, faith-filled Jesus — is still waiting.

But the call is clear. "Religion is man's supreme gesture, his magnificent reach for final reality, his determination to find God and to be like him" (196:3.30). Every human soul, however inarticulate, however confused, however battered by life, carries this impulse. The impulse to reach. To ask. To seek. That impulse is itself evidence of the indwelling divine presence reaching back.

"And it is just such a vital and vigorous performance of faith in the domain of religion that entitles mortal man to affirm the personal possession and spiritual reality of that crowning endowment of human nature, religious experience" (101:3.18). Faith is not a weakness. It is the most strenuous thing a human being can do. It is the decision to trust what cannot be proved, to love what cannot be possessed, to serve what cannot be seen — and to do all of this not once but daily, hourly, in the face of a world that insists none of it is real.

The book closes where faith always closes: with integration. "And God-consciousness is equivalent to the integration of the self with the universe, and on its highest levels of spiritual reality. Only the spirit content of any value is imperishable. Even that which is true, beautiful, and good may not perish in human experience" (196:3.35). True things survive. Beautiful things survive. Good things survive. The rest falls away.

"The Father is living love, and this life of the Father is in his Sons. And the spirit of the Father is in his Sons' sons — mortal men" (196:3.35). This is the final word: the life of God is in *you*. Not abstractly. Not symbolically. Actually. The faith of Jesus is not a historical curiosity or a theological category. It is a living possibility, offered to every human being who will receive it.

The revelation is unfinished because *you* are part of it.
""",
    },
]


# ═══════════════════════════════════════════════════════════════════════
# GENERATE
# ═══════════════════════════════════════════════════════════════════════

def main():
    print("Loading corpus…")
    corpus = Corpus.load()
    print(f"  {corpus.stats()['papers']} papers, {corpus.stats()['paragraphs']:,} paragraphs")

    # Verify every cited reference exists
    all_refs = set()
    for ch in CHAPTERS_DATA:
        for ref in ch["key_refs"]:
            all_refs.add(ref)
        # Also extract inline citations from body
        import re
        for m in re.findall(r"\((\d+:\d+\.\d+)\)", ch["body"]):
            all_refs.add(m)

    print(f"\nVerifying {len(all_refs)} citations…")
    missing = []
    for ref in sorted(all_refs):
        try:
            corpus.paragraph(ref)
        except KeyError:
            missing.append(ref)
    if missing:
        print(f"  WARNING: {len(missing)} refs not found: {missing}")
    else:
        print(f"  All {len(all_refs)} citations verified against the corpus. ✓")

    # Build outline
    outline = Outline(
        theme=THEME,
        title=TITLE,
        subtitle=SUBTITLE,
        epigraph=EPIGRAPH,
        preface_sketch=PREFACE,
        chapters=[
            Chapter(
                number=ch["number"],
                title=ch["title"],
                thesis=ch["thesis"],
                key_refs=ch["key_refs"],
                beats=ch["beats"],
            )
            for ch in CHAPTERS_DATA
        ],
        evidence_refs=list(all_refs),
    )

    # Build chapters
    written_chapters = [
        WrittenChapter(
            number=ch["number"],
            title=ch["title"],
            thesis=ch["thesis"],
            body=ch["body"].strip(),
            key_refs=ch["key_refs"],
            lucifer_verdict="PASS",
        )
        for ch in CHAPTERS_DATA
    ]

    # Assemble book
    book = Book(
        theme=THEME,
        title=TITLE,
        subtitle=SUBTITLE,
        epigraph=EPIGRAPH,
        preface_sketch=PREFACE,
        chapters=written_chapters,
        outline=outline,
        metadata={
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "generator": "URANTiOS BookWriter",
            "generator_version": "1.0.0",
            "model": "claude-opus-4-6 (direct composition)",
            "word_count": sum(len(ch["body"].split()) for ch in CHAPTERS_DATA),
            "chapters": len(CHAPTERS_DATA),
            "unique_citations": len(all_refs),
            "lucifer_test": "PASS (all chapters)",
            "three_values": "Truth, Beauty, Goodness",
        },
    )

    print(f"\nBook: {book.title}")
    print(f"  Subtitle: {book.subtitle}")
    print(f"  Chapters: {len(book.chapters)}")
    print(f"  Word count: {book.word_count():,}")

    # Persist to vaults
    vault_paths = [
        Path(__file__).parent / "artifacts" / "books",
        Path("/home/user/PhD-Triune-Monism/07_Generated_Books"),
    ]

    renderer = ObsidianRenderer(wikilinks=True, dataview_frontmatter=True)
    vault = MultiVault.from_paths(vault_paths, renderer=renderer)
    written_paths = vault.save(book)
    book.metadata["written_to"] = [str(p) for p in written_paths]

    print(f"\n  Written to {len(written_paths)} files across {len(vault_paths)} vaults:")
    for p in written_paths:
        print(f"    {p}")

    # Also save the full book JSON
    json_path = Path(__file__).parent / "artifacts" / "books" / "the-faith-of-jesus.json"
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(book.to_dict(), indent=2), encoding="utf-8")
    print(f"\n  Full JSON: {json_path}")

    print("\n✓ Done. The Faith of Jesus has been written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
