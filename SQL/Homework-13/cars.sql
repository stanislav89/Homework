--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

-- Started on 2020-11-22 23:11:12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 201 (class 1259 OID 16793)
-- Name: car; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.car (
    id integer NOT NULL,
    name character varying(200) DEFAULT 'lore'::character varying NOT NULL,
    year date DEFAULT '1970-01-01'::date NOT NULL
);


ALTER TABLE public.car OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 16791)
-- Name: car_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.car_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.car_id_seq OWNER TO postgres;

--
-- TOC entry 3024 (class 0 OID 0)
-- Dependencies: 200
-- Name: car_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.car_id_seq OWNED BY public.car.id;


--
-- TOC entry 206 (class 1259 OID 16820)
-- Name: car_producer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.car_producer (
    car_id integer DEFAULT 0 NOT NULL,
    producer_id integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.car_producer OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16813)
-- Name: model; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.model (
    id integer NOT NULL,
    info character varying(100) DEFAULT 'unknown'::character varying NOT NULL
);


ALTER TABLE public.model OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16811)
-- Name: model_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.model_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.model_id_seq OWNER TO postgres;

--
-- TOC entry 3025 (class 0 OID 0)
-- Dependencies: 204
-- Name: model_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.model_id_seq OWNED BY public.model.id;


--
-- TOC entry 203 (class 1259 OID 16803)
-- Name: producer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.producer (
    id integer NOT NULL,
    title character varying(200) DEFAULT 'noname'::character varying NOT NULL,
    info_id integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.producer OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16801)
-- Name: producer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.producer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.producer_id_seq OWNER TO postgres;

--
-- TOC entry 3026 (class 0 OID 0)
-- Dependencies: 202
-- Name: producer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.producer_id_seq OWNED BY public.producer.id;


--
-- TOC entry 2866 (class 2604 OID 16796)
-- Name: car id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.car ALTER COLUMN id SET DEFAULT nextval('public.car_id_seq'::regclass);


--
-- TOC entry 2872 (class 2604 OID 16816)
-- Name: model id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.model ALTER COLUMN id SET DEFAULT nextval('public.model_id_seq'::regclass);


--
-- TOC entry 2869 (class 2604 OID 16806)
-- Name: producer id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producer ALTER COLUMN id SET DEFAULT nextval('public.producer_id_seq'::regclass);


--
-- TOC entry 3013 (class 0 OID 16793)
-- Dependencies: 201
-- Data for Name: car; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.car (id, name, year) VALUES (1, 'BMW', '1970-01-01');
INSERT INTO public.car (id, name, year) VALUES (2, 'Renault', '1970-01-01');
INSERT INTO public.car (id, name, year) VALUES (3, 'Ford', '1970-01-01');
INSERT INTO public.car (id, name, year) VALUES (4, 'Skoda', '1970-01-01');
INSERT INTO public.car (id, name, year) VALUES (5, 'Ferrari', '1970-01-01');


--
-- TOC entry 3018 (class 0 OID 16820)
-- Dependencies: 206
-- Data for Name: car_producer; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.car_producer (car_id, producer_id) VALUES (1, 4);
INSERT INTO public.car_producer (car_id, producer_id) VALUES (2, 1);
INSERT INTO public.car_producer (car_id, producer_id) VALUES (3, 3);
INSERT INTO public.car_producer (car_id, producer_id) VALUES (4, 2);


--
-- TOC entry 3017 (class 0 OID 16813)
-- Dependencies: 205
-- Data for Name: model; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.model (id, info) VALUES (1, 'fast');
INSERT INTO public.model (id, info) VALUES (2, 'very_fast');
INSERT INTO public.model (id, info) VALUES (3, 'slow');
INSERT INTO public.model (id, info) VALUES (4, 'space');


--
-- TOC entry 3015 (class 0 OID 16803)
-- Dependencies: 203
-- Data for Name: producer; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.producer (id, title, info_id) VALUES (6, 'Germany', 2);
INSERT INTO public.producer (id, title, info_id) VALUES (7, 'Czech', 0);
INSERT INTO public.producer (id, title, info_id) VALUES (8, 'France', 3);
INSERT INTO public.producer (id, title, info_id) VALUES (9, 'USA', 1);
INSERT INTO public.producer (id, title, info_id) VALUES (10, 'Italy', 2);


--
-- TOC entry 3027 (class 0 OID 0)
-- Dependencies: 200
-- Name: car_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.car_id_seq', 5, true);


--
-- TOC entry 3028 (class 0 OID 0)
-- Dependencies: 204
-- Name: model_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.model_id_seq', 4, true);


--
-- TOC entry 3029 (class 0 OID 0)
-- Dependencies: 202
-- Name: producer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.producer_id_seq', 10, true);


--
-- TOC entry 2877 (class 2606 OID 16800)
-- Name: car car_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.car
    ADD CONSTRAINT car_pkey PRIMARY KEY (id);


--
-- TOC entry 2881 (class 2606 OID 16819)
-- Name: model model_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.model
    ADD CONSTRAINT model_pkey PRIMARY KEY (id);


--
-- TOC entry 2879 (class 2606 OID 16810)
-- Name: producer producer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producer
    ADD CONSTRAINT producer_pkey PRIMARY KEY (id);


-- Completed on 2020-11-22 23:11:12

--
-- PostgreSQL database dump complete
--

