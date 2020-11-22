--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

-- Started on 2020-11-22 17:18:38

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
-- TOC entry 201 (class 1259 OID 16675)
-- Name: films; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.films (
    id integer NOT NULL,
    actor text NOT NULL,
    film text NOT NULL,
    producer character varying(100)
);


ALTER TABLE public.films OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 16673)
-- Name: films_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.films_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.films_id_seq OWNER TO postgres;

--
-- TOC entry 2989 (class 0 OID 0)
-- Dependencies: 200
-- Name: films_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.films_id_seq OWNED BY public.films.id;


--
-- TOC entry 2851 (class 2604 OID 16678)
-- Name: films id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films ALTER COLUMN id SET DEFAULT nextval('public.films_id_seq'::regclass);


--
-- TOC entry 2983 (class 0 OID 16675)
-- Dependencies: 201
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.films VALUES (3, 'J.Depp', 'Pirates', 'Vasya');
INSERT INTO public.films VALUES (4, 'M.Kunis', '1day', 'Petya');
INSERT INTO public.films VALUES (5, 'K.Ostin', 'King2', 'Kolya');
INSERT INTO public.films VALUES (6, 'J.Bane', 'Village', 'I.Son');
INSERT INTO public.films VALUES (7, 'S.Jobs', 'Apple', 'S.Jobs');
INSERT INTO public.films VALUES (8, 'J.Kane', 'Forsage', 'C.Lool');


--
-- TOC entry 2990 (class 0 OID 0)
-- Dependencies: 200
-- Name: films_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.films_id_seq', 8, true);


-- Completed on 2020-11-22 17:18:38

--
-- PostgreSQL database dump complete
--

