/**
* @Brief This file defines some macros to reform the try-catch exception handling mechanism in C++.
		 The original try-catch form maybe some mass and we need a much cheaper way.
		 In parctise,it's so common that such a line code "m_pSession->commit();" would require a lot 
		 try-catch code to handle exceptions.It makes the code hard to read and understand.The runing
		 or the design logic of our programming can be lost with these nondesign lines mixed together.
		 I'm making this file trying to do something to change the situation.

		 The universal result of using the file is here:
		 @Example before
		 void FuncWithException(){
			 string strErrMsg;
			 try{
				...
				task_may_cause_exception();
				...
			 }
			 catch (std::exception& e){
				...
				do_something_to_deal1();
				...
			 }
			 catch (...){
				 ...
				 do_something_to_deal2();
				 ...
			 }
		 }

		 @Example result
		 void FuncWithException(){
			 string strErrMsg;

			 try_catch_exception();

			 ...
			 task_may_cause_exception();
			 ...
			
			catch_xxx_exp();
			 
		 }

		 It's obvious the code get clear.
		 You can easily pick up the main running logic of the programming from these lines.
		 And as you can see below,sometimes it reuses your code,espically when you get a lot of similar catch-deal code.
		 [u may refer ==> #define catch_comm_trans_exp(catch_info) ]

* @Common-Info  Made By Erya 2015.05.28 

*/


#include <string>

using namespace std;

namespace Common
{
	/**
	*@brief 通用宏扩展，try-catch语句入口
	*/
	#define try_catch_exception()  try { 

	/**
	*@brief 通用宏扩展，try-catch语句catch部分
	*/
	#define catch_comm_exp()					\
			}									\
		  catch (std::exception& e) {}			\
		  catch (...) {}						\

	/**
	*@brief SQLite事务进程catch块宏扩展定义
	*/
	#define catch_trans_begin_exp()				catch_comm_trans_exp("transaction begin")
	#define catch_trans_commit_exp()			catch_comm_trans_exp("transaction commit")
	#define catch_trans_rollback_exp()			catch_comm_trans_exp("transaction rollback")

	#define catch_comm_trans_exp(catch_info)															\
		}																								\
		catch (std::exception& e){																		\
			m_pSession->close();																			\
			strErrMsg = e.what();																		\
			strErrMsg = "CSessionDbOpr::" #catch_info "exception,reason:" + strErrMsg;					\
			_LOG_ERROR0("Erya", strErrMsg.c_str());														\
		}																								\
		catch (...){																					\
			strErrMsg = "CSessionDbOpr::" #catch_info ". Unhandled exception";							\
			_LOG_ERROR0("Erya", strErrMsg.c_str());														\
		}																								\

}//namespace Common end

/*****************************************************************************************************
 * A simple example in practise.
 * You can compare the difference between CSessionDbOpr1 and CSessionDbOpr2.
 * This may make the benefit much clearer of using these macro-defined utils.
 
class CSessionDbOpr1{
private:
	SQLiteSession m_pSession;

public:
	void BeginTrans(){
		string strErrMsg;
		try{
			m_pSession->begin();
		}
		catch (std::exception& e){
			m_pSession->close();
			strErrMsg = e.what();
			strErrMsg = "CSessionDbOpr::BeginTrans() exception,reason:" + strErrMsg;
			_LOG_ERROR0("Erya", strErrMsg.c_str());
		}
		catch (...){
			strErrMsg = "CSessionDbOpr::BeginTrans() exception.Unhandled exception";
			_LOG_ERROR0("Erya", strErrMsg.c_str());
		}
	}

	void CommitTrans(){
		string strErrMsg;
		try{
			m_pSession->commit();
		}
		catch (std::exception& e){
			m_pSession->close();
			strErrMsg = e.what();
			strErrMsg = "CSessionDbOpr::CommitTrans() exception,reason:" + strErrMsg;
			_LOG_ERROR0("Erya", strErrMsg.c_str());
		}
		catch (...){
			strErrMsg = "CSessionDbOpr::CommitTrans() exception.Unhandled exception";
			_LOG_ERROR0("Erya", strErrMsg.c_str());
		}
	}

	void RollbackTrans(){
		string strErrMsg;
		try{
			m_pSession->rollback();
		}
		catch (std::exception& e){
			m_pSession->close();
			strErrMsg = e.what();
			strErrMsg = "CSessionDbOpr::RollbackTrans() exception,reason:" + strErrMsg;
			_LOG_ERROR0("Erya", strErrMsg.c_str());
		}
		catch (...){
			strErrMsg = "CSessionDbOpr::RollbackTrans() exception.Unhandled exception";
			_LOG_ERROR0("Erya", strErrMsg.c_str());
		}
	}
}


class CSessionDbOpr2{
private:
	SQLiteSession m_pSession;

public:
	SQLiteSession m_pSession;

	void BeginTrans(){
		string strErrMsg;

		try_catch_exception();

		m_pSession->begin();

		catch_trans_begin_exp();
	}

	void CommitTrans(){
		string strErrMsg;

		try_catch_exception();

		m_pSession->commit();

		catch_trans_begin_exp();
	}

	void RollbackTrans(){
		string strErrMsg;

		try_catch_exception();

		m_pSession->rollback();

		catch_trans_begin_exp();
	}
}
********************************************************************************************/