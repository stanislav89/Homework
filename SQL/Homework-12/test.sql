--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

-- Started on 2020-11-22 18:59:12

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
-- TOC entry 201 (class 1259 OID 16634)
-- Name: people; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.people (
    id integer NOT NULL,
    brand text NOT NULL
);


ALTER TABLE public.people OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 16632)
-- Name: people_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.people_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.people_id_seq OWNER TO postgres;

--
-- TOC entry 2989 (class 0 OID 0)
-- Dependencies: 200
-- Name: people_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.people_id_seq OWNED BY public.people.id;


--
-- TOC entry 2851 (class 2604 OID 16637)
-- Name: people id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.people ALTER COLUMN id SET DEFAULT nextval('public.people_id_seq'::regclass);


--
-- TOC entry 2983 (class 0 OID 16634)
-- Dependencies: 201
-- Data for Name: people; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 2990 (class 0 OID 0)
-- Dependencies: 200
-- Name: people_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.people_id_seq', 1, false);


-- Completed on 2020-11-22 18:59:12

--
-- PostgreSQL database dump complete
--

